# -*- coding: utf-8 -*-
"""
28-DARS JSON

Created on Tue Jan 30 16:13:24 2024

@author: Sunnatillo
"""

import json

# Ma'lumotlarni json ga o'tkazish

x = 10
x_json = json.dumps(x) # bu holatda x str ga o'tkaziladi

y = 5.5
y_json = json.dumps(y)

m = True
m_json = json.dumps(m)

sonlar = (12,45,23,67)
sonlar_json = json.dumps(sonlar)  # bu holatda tuple Arrayga o'tkaziladi

bemorlar = {
    "ism": "Alijon Valiyev",
    "yosh":33,
    'oila':True,
    'farzandlar': ('Ahmad', 'Bonu'),
    'allergiya':None,
    'dorilar': [
        
        {"nomi": "Analgin", 'miqdori':0.5},
        {'nomi':'panadol', 'miqdori':1.2}
        ]
    }

bemorlar_json = json.dumps(bemorlar, indent=4) # bu holatda lug'at str ga o'zgaradi
# print(bemor_json)

# print(bemor.keys())
# print(bemor['farzandlar'])


# json ko'rinishda fayl yaratish

with open('bemor.json', 'w') as f:
    json.dump(bemorlar, f)

bemor2 = json.loads(bemorlar_json) # json dan pythonga o'tkazish

# json faylni paythonga o'zgartirish
file_name = 'bemor.json'
with open(file_name) as f:
    bemor = json.load(f)



