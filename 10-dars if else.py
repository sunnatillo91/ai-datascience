# -*- coding: utf-8 -*-
"""
10-DARS IF ELSE shartlari va Tarmoqlanish

Created on Sat Dec 23 20:37:28 2023

@author: Sunnatillo
"""

avtolar = ["audi", "bmw", "kia", "lacetti"]
for avto in avtolar:    #avtolar ichidagi har bir avto uchun
    if avto == "bmw":   #agar avto bmw bo'lsa
        print(avto.upper())     #hamma harf katta bo'lsin
    else:                       #aks holda
        print(avto.title())     #faqat birinchi harfi katta bo'lsin
        
ism = 'Ali'
ism.lower() == 'ali'

ism = input("Ismingiz nima? >>> \n")
if ism.lower() != 'ali':
    print(f"Assalomu alaykum, {ism.title()}, uzr biz Alini kutayapmiz")
else:
    print("Salom Ali")

javob = float(input("12*6 nechaga teng?>>> "))
if javob != 72:
    print("Javob noto'g'ri")

yosh = int(input("Yoshingiz nechada?>>>"))
if yosh >= 18:
    print("Xush kelibsiz")
else:
    print("Kirish mumkin emas")

login = input("Yangi login tanlang>>> ")
if len(login) <= 5:   # login uzunligini tekshiramiz
    print("Login kamida 6 ta belgidan iborat bo'lishi kerak")
    
t_yil = int(input("Tug'ilgan yilingizni kiriting>>> "))
if 2023-t_yil >=18:
    print(f"Siz {2023-t_yil} yoshda ekansiz")
    print("Xush kelibsiz")
else:
    print("Siz 18 yoshdan kichik ekansiz. Sizga kirish mumkin emas!")

yosh = int(input("Yoshingiz nechada? >>>"))
if yosh >= 65:
    print("Siz COVID-19 risk guruhida ekansiz.")

x, y = 450, 50
print("x>y") if x>y else print("x<y")
    
    