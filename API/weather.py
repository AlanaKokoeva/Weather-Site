import requests, json
from .settings import *


def get_weather(city):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=1&aqi=no&alerts=no"
    json_data = requests.get(url).text
    data = json.loads(json_data)
   
    city = data["location"]["name"] 
    temp = data["current"]["temp_c"]
    text = data["current"]["condition"]["text"]
    hourly = data["forecast"]["forecastday"][0]["hour"]
    weather = {"city" : city, "hourly" : hourly, "temp" : temp, "text" : text}
    return weather
# http://api.weatherapi.com/v1/forecast.json?key=1a65bf7737534632a1d172625212911&q=Barcelona&days=1&aqi=no&alerts=no
# location		
#   name	"Barcelona"
#   region	"Catalonia"
#   country	"Spain"
#   tz_id	"Europe/Madrid"
#   localtime_epoch	1638207789
#   localtime	"2021-11-29 18:43"
#   icon	"//cdn.weatherapi.com/weather/64x64/night/113.png"
#   date	"2021-11-29"
#   icon	"//cdn.weatherapi.com/weather/64x64/day/113.png"
#   hour    0
#   time	"2021-11-29 00:00"
# current  
#   temp_c 	7
# condition
#   text	"Sunny"