# -*- coding: utf-8 -*-
"""
16-amaliyot
Created on Thu Jan  4 21:34:48 2024

@author: Sunnatillo
"""

# AMALIYOT

# - Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxslar haqidagi ma'lumotlarni lug'at 
#  ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
buxoriy = {
    'ism':'Abu Abdulloh Muhammad ibn Ismoil ibn Ibrohim al Buxoriy',
    'tyil':810,
    'kitoblari':["Al-jomeʼ as-sahih",  "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sagʻir"]
    }
temur = {
    'ism':'Amir Temur',
    'tyil':1336,
    'kitoblari':["temur tuzuklari", "temur tuzuklari", "temur tuzuklari"]
    }
bobur = {
    'ism':'Zahiriddin muhammad bobur',
    'tyil':1483,
    'kitoblari':["Xatti Boburiy","Boburnoma", 'mubayyin']
    }
shayx = {
    'ism':'shayx muhammad sodiq muhammad yusuf',
    'tyil':1952,
    'kitoblari':["tafsiri hilol", "kifoya", "yolg'on"]
    }
mashxurlar = [buxoriy, temur, bobur, shayx]
# for mashxur in mashxurlar:
#     print(f"{mashxur}")

# - Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. For tsikli yordamida 
# muallifning ismi va uning asarlarini konsolga chiqaring.
# for mashxur in mashxurlar:
#     print(f"\n{mashxur['ism']} asarlari: {mashxur['kitoblari']}")
# - Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit, 
# uning sevimli kinolarini esa ro'yxat ko'rinishida lug'atga saqlang.  Natijani konsolga chiqaring.
kinolar = {
    'ali':['abdulhamid', 'yunus emro', 'shaytanat'],
    'vali':['bobur', 'navoiy', 'terminator'],
    'salim':['yulduzli tunlar', 'matrix', 'haker']
    }
# for ism, info in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari: ")
#     for kino in info:
#         print(kino.title())
# - Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at 
# ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.
davlatlar = {
    "o'zbekiston":{'poytaxti':'Toshkent',
                   "maydoni": "— 448,978 km2.",
                   "aholisi soni":"36 milliondan ortiq",
                   "pul birligi":"— soʻm.",},
    
    "qozogʻiston":{'poytaxti':'Ostona',
                   "maydoni": "— 2 million 724,9 ming km² ",
                   "aholisi soni":"19,17 mln. kishi ",
                   "pul birligi":"— Tenge"},
    
    "turkmaniston":{'poytaxti':'Ashxobod',
                   "maydoni": "— 488,100 km2",
                   "aholisi soni":"6 million",
                   "pul birligi":"— Manat "},
                   }
# for davlat, info in davlatlar.items():
#     print(f"{davlat} - poytaxti {info['poytaxti']}, maydoni {info['maydoni']}, aholisi {info['aholisi soni']}, pul birligi {info['pul birligi']}")

# - Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan 
# davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida 
# ma'lumot yo'q" degan xabarni chiqaring.

mamlakat = input("Istalgan davlat nomini kiriting: ")

for davlat, info in davlatlar.items():
    if davlat == mamlakat:
        print(f"{davlat.title()} - poytaxti {info['poytaxti']}, maydoni {info['maydoni']}, aholisi {info['aholisi soni']}, pul birligi {info['pul birligi']}")

