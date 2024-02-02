# -*- coding: utf-8 -*-
"""
20-dars FUNKSIYADAN QIYMAT QAYTARISH

Created on Wed Jan 10 18:35:01 2024

@author: Sunnatillo
"""
def avto_info(kompaniya, model, rangi, korobka, yili, narxi = None):
    avto = {
        'kompaniya':kompaniya,
        'model':model,
        'rangi':rangi,
        'korobka':korobka,
        'yili':yili,
        'narxi':narxi
        }
    return avto

avto1 = avto_info('GM', "Cobalt", "Qora", "avtomat", 2023)
avto2 = avto_info("GM", "Malibu", "Oq", "Avtomat", 2022, 22000)
avtolar = [avto1, avto2]
print("Onlayn bozorlardagi mavjud mashinalar: ")
for avto in avtolar:
    if avto['narxi']:
        narx = avto['narxi']
    else:
        narx = "Noma'lum"
    print(f"{avto['rangi']} {avto['model']} narxi: {narx}")