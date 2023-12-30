# -*- coding: utf-8 -*-
"""
16-DARS Nesting
Created on Sat Dec 30 12:56:03 2023

@author: Sunnatillo
"""

car0 = {
        'model':'cobalt',
        'rang':'oq',
        'yil':2022,
        'narx':14000,
        'km':150,
        'korobka':'avtomat'
        }
car1 = {
        'model':'gentra',
        'rang':'oq',
        'yil':2021,
        'narx':14500,
        'km':150,
        'korobka':'avtomat'
        }
car2 = {
        'model':'spark',
        'rang':'oq',
        'yil':2021,
        'narx':12000,
        'km':150,
        'korobka':'avtomat'
        }

# car = car0
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narx']}$")

# car = car1
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narx']}$")    

cars = [car0, car1, car2]  # lug'atlar ro'yxat ichiga joylashtirildi va kodlar ham qisqartirilib bir xil natija olindi
# for car in cars:
#     print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narx']}$")    
    
# cars[0]['model']  #bu orqali cars ro'yxatidagi 0- lugatning model degan kalit so'ziga murojaat qilib uning qiymati olindi

print(f"{cars[1]['rang'].title()} "
      f"{cars[1]['model'].title()}")

malibus = []
for n in range(10):
    new_car = {
        'model':'malibu',
        'rangi':None,
        'yili':2022,
        'narx':None,
        'km':0,
        'korobka':'avtomat'
        }
    malibus.append(new_car)

for malibu in malibus[0:3]:
    malibu['rangi']='qizil'

# for malibu in malibus:
#     print(malibu)

for malibu in malibus[3:6]:
    malibu['rangi']='qora'

for malibu in malibus[6:]:
    malibu['rangi']='oq',
    malibu['korobka']='mexanika'

for malibu in malibus:
    if malibu['korobka']=='avtomat':
        malibu['narx']=40000
    else:
        malibu['narx']=35000


for malibu in malibus:
    print(malibu)
    
    
# LUG'AT ICHIDA RO'YXAT
dasturchilar = {
    'ali':['python', 'c++'],
    'vali':['java', 'c#'],
    'maruf':['php', 'javascript'],
    'sunnatillo':['php', 'python']
    }
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi: ")
    for til in tillar:
        print(f"{til.upper()} ", end='')

# LUG'AT ICHIDA LUG'AT
hamkasblar = {
    'ali':{'familya':'valiyev',
           'tyil':2005,
           'malumot':'oliy',
           'tillar':['python', 'c++']
           },
    'vali':{'familya':'boliyev',
           'tyil':2000,
           'malumot':'oliy',
           'tillar':['php', 'c#']
           },
    'salim':{'familya':'nosirov',
           'tyil':2001,
           'malumot':'oliy',
           'tillar':['python', 'php']
           }
    }

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familya'].title()}, "
          f"{info['tyil']}-yil da tug'ilgan "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi: ")
    for til in info['tillar']:
        print(til.upper())
          
# AMALIYOT

# - Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxslar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. 
# Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
buxoriy = {
    'ism':'Abu Abdulloh Muhammad ibn Ismoil ibn Ibrohim al Buxoriy',
    'tyil':810,
    'kitoblari':'Sahihul Buxoriy'
    }
temur = {
    'ism':'Amir Temur',
    'tyil':1336,
    'kitoblari':"temur tuzuklari"
    }
bobur = {
    'ism':'Zahiriddin muhammad bobur',
    'tyil':1483,
    'kitoblari':'mubayyin'
    }
shayx = {
    'ism':'shayx muhammad sodiq muhammad yusuf',
    'tyil':1952,
    'kitoblari':'tafsiri hilol, kifoya'
    }
mashxurlar = [buxoriy, temur, bobur, shayx]
for mashxur in mashxurlar:
    print(f"\nTo'liq ismi {mashxur['ism'].title()}, "
          f"{mashxur['tyil']}-yilda tug'ilgan. "
          f"Yozgan kitoblari: {mashxur['kitoblari'].title()}")
# - Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. For tsikli yordamida muallifning ismi 
# va uning asarlarini konsolga chiqaring.

# - Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.  Natijani konsolga chiqaring.

# - Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.

# - Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
    