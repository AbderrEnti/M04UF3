#!/usr/bin/python3

import requests
import gspread
from colorama import Fore, Style, init
init()

print(Fore.YELLOW + "Buscador de películas" + Style.RESET_ALL)
movie_title = input("Introduce el título de la película a buscar: ")
url="https://search.imdbot.workers.dev/?q="+movie_title

movie = requests.get(url)
data = movie.json()

if 'description' in data:
	movie_data = data['description'][0]
	title = movie_data.get ('#TITLE', 'No disponible')
	year = movie_data.get ('#YEAR', 'No disponible')
	actors = " ".join(movie_data.get ('#ACTORS', []))

	print(Fore.GREEN + f" {title}" + Style.RESET_ALL)
	print(Fore.GREEN + f" {year}" +Style.RESET_ALL)
	print(Fore.GREEN + f" {actors}" + Style.RESET_ALL)

	gc = gspread.service_account()
	sh = gc.open("Pelis")
	worksheet = sh.sheet1

	worksheet.append_row([title, year, actors])
	print(Fore.GREEN + "Has agregado la información de la peli a google sheet" + Style.RESET_ALL)
else:
	print(Fore.REDE + "La información no se ha agregado correctamente a google sheets" +Style.RESET_ALL)
