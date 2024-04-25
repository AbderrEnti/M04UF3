#!/usr/bin/python3

import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=41.382274191583036&longitude=2.1166885842478287&current=temperature_2m"

weather_enti = requests.get(url)
data = weather_enti.json()
temp = data['current']['temperature_2m']
units = data['current_units']['temperature_2m']

print(f"La temperatura en Enti es: {temp} {units}")
