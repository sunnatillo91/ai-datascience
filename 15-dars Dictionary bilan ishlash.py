# -*- coding: utf-8 -*-
"""
15-DARS LUG'ATlar bilan ishlash 

Created on Thu Dec 28 19:20:24 2023

@author: Sunnatillo
"""

talaba_0 = {'ism':'murod olimov', 'yosh':20, 't_yil':2003}

print(talaba_0.items())

for kalit, qiymat in talaba_0.items(): # bu yo'l bilan kalit va qiymatlarni chiqarish mumkin
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat} \n")
    
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'salim':'nokia 3110'
    }

for k, q in telefonlar.items():
    print(f"{k}ning telefoni {q}")
    
mahsulotlar = {'olma':15000, 'uzum':20000, 'shaftoli':18000, 'nok':25000}
print("Do'kondagi mahsulotlar: ")
for mahsulot in mahsulotlar.keys():   # mahsulotlar ichidagi kalit so'zlarni konsolga chiqaradi
# for mahsulot in mahsulotlar: # ko'rinishida yozsa ham bo'ladi
    print(mahsulot.title())
    
bozorlik = ['anor', 'uzum', 'non', 'baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
        
for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Iltimos do'koningizga {buyum} ham olib keling")
        
# # LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH
print("Do'konimizdagi mahsulotlar: ")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())
    
# .values() lug'at qiymatlarini qaytaradi
print(telefonlar.values())
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'salim':'nokia 3110',
    'umar':'iphone x',
    'muhammad':'galaxy s9',
    'kozim':'mi 10 pro',
    }

print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi: ")
for tel in telefonlar.values():
    print(tel)

# # set bir xil qiymatlarni takrorlanishini oldini olish uchun foydalanamiz.
print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi: ")
for tel in set(telefonlar.values()):
    print(tel)
    
toys = {'ball', 'car', 'lamp', 'ball', 'bear', 'car'}  # turi set va buni consolga chiqarganda 
# takrorlangan elementlarni chiqarmaydi
print(toys)

# AMALIYOT

# - Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va 
# qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 
python_dictionary = {
    'print':'consolga chiqarish funksiyasi',
    'consol':'Spyder muhitida ishchi oyna',
    'spyder':'Python dasturlash tili uchun maxsus integratsion muhit',
    'integer':'butun son',
    'float':'o\'nlik son',
    'string':'matn',
    'if':'maxsus shartlar',
    'else':'aks holda',
    'for':'uchun',
    'dictionary':'lug\'at'
    }
for k, q in sorted(python_dictionary.items()):
    print(f"Pythonda {k} {q}ni bildiradi")
# - Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni 
# alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 
poytaxtlar = {
    'Toshkent':'Uzbekistan',
    'Andorra-la-Velya':'Andorra',
    'Afina':'Gretsiya',
    'Belgrad':'Serbiya',
    'Berlin':'Germaniya',
    'Bern':'Shveysariya',
    'Bratislava':'Slovakiya',
    'Brussel':'Belgiya',
    'Budapesht':'Vengriya',
    'Buxarest':'Ruminiya',
    'Dublin':'Irlandiya',
    'Kiyev':'Ukraina' 
    }
for davlat in sorted(poytaxtlar.values()):
    print(davlat)
print(' ')
for poytaxt in sorted(poytaxtlar.keys()):
    print(poytaxt)
# - Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. 
# Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
dav = poytaxtlar.get(input("Istalgan davlatingiz nomini kiriting:>>> "), "Bizda bunday ma'lumot yo'q")
print(dav)
# - Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat 
# buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa 
# narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

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
print("Assalomu alaykum, uchta ovqat buyurtma bering:")
for taom in range(3):
    buyurtma.append(input(f"{taom+1}-taom>>> "))
    
for taom in buyurtma:
    if taom in menu:
        print(f"{taom} narxi {menu[taom]} so'm")
    else:
        print(f"{taom} - bizda bunday taom yo'q")
        
