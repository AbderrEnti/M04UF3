#!/usr/bin/python3
 
import gspread

gc = gspread.service_account()

sh = gc.open("Fary's adventures")

print(sh.sheet1.get('A1'))
