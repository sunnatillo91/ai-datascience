# -*- coding: utf-8 -*-
"""
15-amaliyot
Created on Thu Jan  4 19:12:58 2024

@author: Sunnatillo
"""

# AMALIYOT

# - Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va 
# qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 
dict_py = {
    'print':'Ma\'lumotni konsolga chiqarish',
    'variables':'o\'zgaruvchilar',
    'string':'matn',
    'integer':'butun son',
    'float':'o\'nlik son',
    'list':'ro\'yxat',
    'console':'spyderda natijani ko\'rsatadigan oyna',
    'spyder':'dasturlash muhiti',
    'dictionary':'lug\'at'
    }
# for k, v in sorted(dict_py.items()):
#     print(f"{k}ning qiymati {v}")
# - Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni 
# alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 
poytaxtlar = {
    'Uzbekistan':'Toshkent',
    'Andorra':'Andorra-la-Velya',
    'Gretsiya':'Afina',
    'Serbiya':'Belgrad',
    'Germaniya':'Berlin',
    'Shveysariya':'Bern',
    'Slovakiya':'Bratislava',
    'Belgiya':'Brussel',
    'Vengriya':'Budapesht',
    'Ruminiya':'Buxarest',
    'Irlandiya':'Dublin',
    'Ukraina':'Kiyev' 
    }
# for k in sorted(poytaxtlar):
#     print(k)
# print('')
# for v in sorted(poytaxtlar.values()):
#     print(v)

# # - Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. 
# # Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
# davlat = poytaxtlar.get(input("Istalgan davlat nomini kiriting:>>> ").title(), "Bizda bunday ma'lumot yo'q")
# print(davlat)
# for dav in poytaxtlar:
#     if dav == davlat.title():
#        print(f"{dav} poytaxti {poytaxtlar[dav]}")
# # - Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta 
# # ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda 
# # bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

menu = {
        'osh':25000,
        'kabob':55000,
        'manti':18000,
        'lag\'mon':15000,
        'somsa':8000,
        'kfc':55000,
        'baliq':80000,
        'tabaka':45000,
        'barak':22000,
        'tuxumbarak':13000,
        'sho\'rva':20000
        }
buyurtma = []
print("Uchta taom buyurtma bering:>>> ")
for n in range(3):
    buyurtma.append(input(f"{n+1}-taom>> "))

for taom in menu:
    if taom in buyurtma:
        print(f"{taom} narxi {menu[taom]} so'm")
for taom in buyurtma:
    if taom not in menu:
        print(f"{taom} bizda bunday taom yo'q")
    
    
    

