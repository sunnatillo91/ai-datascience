# -*- coding: utf-8 -*-
"""
28-dars JSON Practise

Created on Tue Jan 30 20:11:44 2024

@author: Sunnatillo
"""
import json

# AMALIYOT
# 1. Ushbu o'zgaruvchini JSON ko'rinishida saqlang va JSON matnini konsolga chiqaring: 
#     data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data_json = json.dumps(data)
# print(data_json)

# 2. Ushbu JSON matnni ko'chirib oling, va talabaning ismi va familiyasini  konsolga 
#  chiqaring: talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}""" 

talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}""" 
talaba = json.loads(talaba_json)
print(talaba.keys())
ism = talaba['ism']
familiya = talaba['familiya']
print(ism, familiya)
# 3. Yuqoridagi ikki o'zgaruvchini alohida JSON fayllarga saqlang.
with open('talaba.json', 'w') as f:
    json.dump(talaba, f)
    
with open('data.json', 'w') as f:
    json.dump(data, f)
# 4. Quyidagi JSON faylni yuklab oling. Faylda 3 ta talabaning ism va familiyasi saqlangan. 
# Ularning har birini alohida qatordan "Ism Familiya, n-kurs, Fakultet talabasi" 
# ko'rinishida konsolga chiqaring.

