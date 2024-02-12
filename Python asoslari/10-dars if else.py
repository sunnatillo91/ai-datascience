# -*- coding: utf-8 -*-
"""
10-DARS IF ELSE shartlari va Tarmoqlanish

Created on Sat Dec 23 20:37:28 2023

@author: Sunnatillo
"""

# avtolar = ["audi", "bmw", "kia", "lacetti"]
# for avto in avtolar:    #avtolar ichidagi har bir avto uchun
#     if avto == "bmw":   #agar avto bmw bo'lsa
#         print(avto.upper())     #hamma harf katta bo'lsin
#     else:                       #aks holda
#         print(avto.title())     #faqat birinchi harfi katta bo'lsin
        
# ism = 'Ali'
# ism.lower() == 'ali'

# ism = input("Ismingiz nima? >>> \n")
# if ism.lower() != 'ali':
#     print(f"Assalomu alaykum, {ism.title()}, uzr biz Alini kutayapmiz")
# else:
#     print("Salom Ali")

# javob = float(input("12*6 nechaga teng?>>> "))
# if javob != 72:
#     print("Javob noto'g'ri")

# yosh = int(input("Yoshingiz nechada?>>>"))
# if yosh >= 18:
#     print("Xush kelibsiz")
# else:
#     print("Kirish mumkin emas")

# login = input("Yangi login tanlang>>> ")
# if len(login) <= 5:   # login uzunligini tekshiramiz
#     print("Login kamida 6 ta belgidan iborat bo'lishi kerak")
    
# t_yil = int(input("Tug'ilgan yilingizni kiriting>>> "))
# if 2023-t_yil >=18:
#     print(f"Siz {2023-t_yil} yoshda ekansiz")
#     print("Xush kelibsiz")
# else:
#     print("Siz 18 yoshdan kichik ekansiz. Sizga kirish mumkin emas!")

# yosh = int(input("Yoshingiz nechada? >>>"))
# if yosh >= 65:
#     print("Siz COVID-19 risk guruhida ekansiz.")

# x, y = 450, 50
# print("x>y") if x>y else print("x<y")
    
    
# AMALIYOT

# - Yangi `cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']` degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring.
#  `GM` uchun ikkala harfni katta qiling.
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())
# - Yuqoridagi mashqni teng emas (`!=`) operatori yordamida bajaring. 
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())
# - Foydalanuvchi login ismini so'rang. Agar login `admin` bo'lsa, `"Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?"` 
# xabarini konsolga chiqaring. Aks holda, `"Xush kelibsiz, {foydalanuvchi_ismi}!"`  matnini konsolga chiqaring.
# logins = input("Login kiriting >>> ")
# if logins.lower() == 'admin':
#    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#    print(f"Xush kelibsiz, {logins}!")    

# - Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, `"Sonlar teng"` ekan degan yozuvni konsolga chiqaring.
# print("Istalgan ikkita son kiriting.")
# son1 = input("1-son: >>>")
# son2 = input("2-son: >>> ")
# if son1 == son2:
#     print("Sonlar teng ekan")
          
# - Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga `"Manfiy son"`, agar musbat bo'lsa `"Musbat son"` degan xabarni chiqaring. 
print("Istalgan son kiriting.")
son1 = input("son: >>>")
if son1 <= 0:
    print("Manfiy son")
else:
    print("")
# - Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, `"Musbat son kiriting"` degan xabarni chiqaring. 