#!/usr/bin/python3

import requests

url = "https://search.imdbot.workers.dev/?q="
movie_name = input("Introduce el nombre de una película: ")
full_url = url + movie_name
response = requests.get(full_url)
