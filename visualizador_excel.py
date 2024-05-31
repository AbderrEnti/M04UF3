#!/usr/bin/python3
import gspread
import re
import csv
import pandas as pd

gc = gspread.service_account()
sh_dmesg = gc.open("dmesg")

worksheet_list = sh_dmesg.worksheets()
fechas = [word.title for word in worksheet_list]
fechas_ordenadas = sorted(fechas, reverse=True)
mayores = fechas_ordenadas[:5]
for idx, fecha in enumerate(mayores, 1):
	    print(f"{idx}: {fecha}")

user = int(input("¿Qué fecha deseas seleccionar (1-5)?: "))

fecha_deseada = mayores[user - 1]
            
lista_deseada = sh_dmesg.worksheet(fecha_deseada).get_all_values()

input_menu = int(input("¿Qué acción deseas realizar? (1. Buscar Palabra, 2. Copia de Seguridad): "))

if input_menu == 1:
	user_search = input("Introduce la palabra que deseas buscar: ")
	for array in lista_deseada:
		if re.search(user_search, array[1], re.IGNORECASE):
			print(f"Este array contiene la palabra: {array}")
            
elif input_menu == 2:
	nombre = "copia_seguridad.csv"
	with open(nombre, 'w', newline='') as archivo_csv:
		escrior_csv = csv.writer(archivo_csv)
		for arrays in lista_deseada:
			escrior_csv.writerow(arrays)
		print("Copia de seguridad creada con éxito.")
else:
	print("Opción no válida")
