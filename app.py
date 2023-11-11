from flask import Flask, render_template, url_for, redirect, session, abort
import requests
import json
import datetime as dt
from authlib.integrations.flask_client import OAuth
from geolite2 import geolite2
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from unidecode import unidecode

app = Flask(__name__)

appConf = {
    "OAUTH2_CLIENT_ID": "564598204141-cmcgu790m0mq4jnaj1hna2cqj0g5k7kt.apps.googleusercontent.com",
    "OAUTH2_CLIENT_SECRET": "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",
    "OAUTH2_META_URL": "https://accounts.google.com/.well-known/openid-configuration",
    "FLASK_SECRET": "ec16d517-c992-4697-a1f3-df5346b321a3",
    "FLASK_PORT": 5000
}

app.secret_key = appConf.get("FLASK_SECRET")

oauth = OAuth(app)

oauth.register(
    "GoogleOAuth",
    client_id=appConf.get("OAUTH2_CLIENT_ID"),
    client_secret=appConf.get("OAUTH2_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email https://www.googleapis.com/auth/user.birthday.read https://www.googleapis.com/auth/user.gender.read",
    },
    server_metadata_url=f'{appConf.get("OAUTH2_META_URL")}',
)

# Função responsável por retornar a latitude e a longitude de uma determinada cidade
def get_lat_lon(city_name):
    url = f"https://nominatim.openstreetmap.org/search?city={city_name}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            latitude = float(data[0]['lat'])
            longitude = float(data[0]['lon'])
            return latitude, longitude
        else:
            return None
    else:
        return None   

# Rota padrão da homepage         

@app.route('/')
def homepage():
    # IP do usuário
    request = requests.get('https://checkip.amazonaws.com')
    ip = request.text[:-2]

    # Data
    date = dt.datetime.now().strftime('%d / %m / %Y')

    # Localização
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    result = response.json()
    location = {'cidade': result['city'],
                'estado': result['region']}
    
    # Clima
    owm = OWM('dcd035bef80eaba0aa59b0aa27616c49')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(f'{location['cidade']}, BR')
    air_mgr = owm.airpollution_manager()
    air_obs = air_mgr.air_quality_at_coords
    w = observation.weather

    # Dicionário com todas as informações do clima
    clima = {'status': w.status,
             'detailed_status': w.detailed_status,
             'vento': w.wind(),
             'umidade': w.humidity,
             'temperatura' : (w.temperature('celsius')),
             'chuva' : w.rain,
             'nuvem': w.clouds,
             'pressao': w.barometric_pressure(),
             'nascer': w.sunrise_time(),
             'por': w.sunset_time(),
             }   

    #Poluentes
    latitude, longitude = get_lat_lon(location['cidade'])
    pol_mgr = owm.airpollution_manager()
    air_status = pol_mgr.air_quality_at_coords(latitude, longitude) 

    return render_template('index.html', ip=ip, date=date, location=location, clima = clima, poluentes=air_status, session=session.get("user"),
                           pretty=json.dumps(session.get("user"), indent=4))

@app.route("/signin-google")
def googleCallback():
    token = oauth.GoogleOAuth.authorize_access_token()
    personDataUrl = "https://people.googleapis.com/v1/people/me?personFields=genders,birthdays"
    personData = requests.get(personDataUrl, headers={
        "Authorization": f"Bearer {token['access_token']}"
    }).json()
    token["personData"] = personData
    session["user"] = token
    return redirect(url_for("homepage"))


@app.route("/google-login")
def googleLogin():
    if "user" in session:
        abort(404)
    return oauth.GoogleOAuth.authorize_redirect(redirect_uri=url_for("googleCallback", _external=True))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("homepage"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=appConf.get("FLASK_PORT"), debug=True)