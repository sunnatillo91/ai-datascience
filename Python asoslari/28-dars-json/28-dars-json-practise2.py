# -*- coding: utf-8 -*-
"""
28-dars JSON Practise

Created on Tue Jan 30 21:13:19 2024

@author: Sunnatillo
"""

import json

# 4. Quyidagi JSON faylni yuklab oling. Faylda 3 ta talabaning ism va familiyasi saqlangan. 
# Ularning har birini alohida qatordan "Ism Familiya, n-kurs, Fakultet talabasi" 
# ko'rinishida konsolga chiqaring.

# file_path = r'd:\programming\ai-datacsience\28-dars-json\students.json'
file_path = 'students.json'

try:
    with open(file_path, 'r') as file:
        data = json.load(file)
        # Process the data as needed
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

a = data['student'][:]

for talaba in a:
    info = f"{talaba['name']} {talaba['lastname']}, {talaba['year']}-kurs,"
    info += f"{talaba['faculty']} talabasi"
    print(info)