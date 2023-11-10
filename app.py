from flask import Flask, render_template, url_for, redirect, session
import requests
import json
import datetime as dt
from geolite2 import geolite2
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from unidecode import unidecode

app = Flask(__name__)

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

    return render_template('index.html', ip=ip, date=date, location=location, clima = clima, poluentes=air_status, email=email)

if __name__ == '__main__':
    app.run(debug=True)