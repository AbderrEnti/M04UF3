#!/usr/bin/python3

import gspread 

gc = gspread.service_account()

 sh = gc.open("Pelis")

print(sh.sheet1.get('A1'))


