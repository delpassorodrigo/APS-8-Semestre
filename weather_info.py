import datetime as dt
import requests

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
API_KEY = 'dcd035bef80eaba0aa59b0aa27616c49'
CITY = 'Américo Brasiliense'

url = BASE_URL + 'appid=' + API_KEY + "&q=" + CITY

data = requests.get(url).json()

surface_temp = data['main']['temp']
altitude_temp = data['main']['temp_at_1000m']

print(surface_temp)
print(altitude_temp)