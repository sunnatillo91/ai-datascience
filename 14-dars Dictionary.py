# -*- coding: utf-8 -*-
"""
14-DARS: Dictionary: Lug'at

Created on Wed Dec 27 21:58:16 2023

@author: Sunnatillo
"""

# car_0 = {'model':'ferrari', 'rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])

# en_uz = {'apple':'olma', 'banana':'banan', 'tomato':'pomidor'}

# talaba_0 = {'ism':'murod olimov', 'yosh':20, 't_yil':2003}

# print(f"{talaba_0['ism'].title()}, \
# {talaba_0['t_yil']}-yilda tug'ilgan, \
# {talaba_0['yosh']} yoshda")

# Yangi kalit so'z va qiymat qo'shish
# talaba_0['kurs'] = 3
# talaba_0['fakultet'] = 'informatika'
# talaba_0['ism'] = 'abdulloh'      # lug'atdagi qiymatlarni ham shu tartibda o'zgartirish mumkin

# Bo'sh lug'at yaratish
# talaba_1 = {}
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 2
# talaba_1['yosh'] = 22
# print(f"{talaba_1['ism'].title()}, {talaba_1['kurs']}-kurs, {talaba_1['yosh']} yoshda")

# Qiymatni yangilash
# talaba_1['kurs'] = 4
# print(f"Talaba {talaba_1['ism'].title()}, {talaba_1['kurs']}-kurs, {talaba_1['yosh']} yoshda")

# # Kalit so'z-qiymat ni o'chirib tashlash
# talaba_0 = {'ism':'murod olimov', 'yosh':20, 't_yil':2003}
# print(talaba_0)
# del talaba_0['yosh']
# print(talaba_0)

# Lug'atlarni bir necha qatorda yozish
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'salim':'nokia 3110'
#     }
# phone = telefonlar.get('hasan', 'Bunday ism mavjud emas')  # telefonlar lug'atida kalit so'z (masalan 'hasan') bilan get metodi yordamida qidiriladi
# # agar chiqmasa 'Bunday ism mavjud emas' xabari qaytariladi
# print(phone) 

# AMALIYOT
# - otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting 
# (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: `Otamning ismi Mavlutdin, 
#  1954-yilda, Samarqand viloyatida tug'ilgan`
# otam = {'ism':'yigitali ochilov', 't_yil':1966, 'viloyat':'samarqand', 'tuman':'narpay'}
# print(f"Otam {otam['ism'].title()} {otam['t_yil']}-yilda {otam['viloyat'].title()} viloyatida tug'ilgan")
# onam = {'ism':'ro\'zibuvi ochilova', 't_yil':1969, 'viloyat':'samarqand', 'tuman':'narpay'}
# print(f"Onam {onam['ism'].title()} {onam['t_yil']}-yilda {onam['viloyat'].title()} viloyatida tug'ilgan")
# opam = {'ism':'malika ochilova', 't_yil':1989, 'viloyat':'samarqand', 'tuman':'narpay'}
# print(f"Opam {opam['ism'].title()} {opam['t_yil']}-yilda {opam['viloyat'].title()} viloyatida tug'ilgan")
# - Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining 
# sevimli taomini konsolga chiqaring: `Alining sevimli taomi osh`
# taomlar = {
#     'ali':'osh',
#     'vali':'baliq',
#     'moxinur':'somsa',
#     'umar':'sous',
#     'muhammad':'sut'
#     }
# print(f"Moxinurning sevimli taomi {taomlar['moxinur']}")
# print(f"Umarning sevimli taomi {taomlar['umar']}")
# print(f"Muhammadning sevimli taomi {taomlar['muhammad']}")
# - Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if,
# else va hokazo) va har birining qisqacha tarjimasini yozing.
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
# - Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda
# mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
jumla = input("Python bo'yicha biror so'z kiriting>>> ")
if jumla in python_dictionary:
    py_dict = python_dictionary.get('jumla', "Bunday so'z mavjud emas")
    print(py_dict)
# - Yuqoridagi vazifani `if-else` yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.










