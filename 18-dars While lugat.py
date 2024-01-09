# -*- coding: utf-8 -*-
"""
18-dars While() list va Lug'atlar
Created on Mon Jan  8 21:13:19 2024

@author: Sunnatillo
"""

# print("Yaqin do'stlaringiz ismini kiriting")
# ismlar = []
# n = 1
# ishora = True
# while ishora:
#     savol = f"{n}-do'stingiz ismi>> "
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism kiritasizmi? >> (ha/yo'q) ")
#     n += 1
#     if takrorlash == 'yo\'q':
#         break
# print(f"Do'stlaringiz ro'yxati: {ismlar}")
    

# print("Do'stlaringiz yoshini saqlaymiz")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input("Do'stingiz yoshini kirititng: ")
#     dostlar[ism] = int(yosh)
#     takror = input("Yana ma'lumot kiritasizmi? ha/yo'q ")
#     if takror == "yo'q":
#         break
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")
    
# cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'audi', 'malibu', 'nexia']

# while 'nexia' in cars:
#     cars.remove('nexia')
# print(cars)

# cars = ['lacetti', 'nexia', 'toyota', 'nexia','lacetti','lacetti','audi', 'malibu', 'nexia']
# car = 'lacetti'
# while car in cars:
#     cars.remove(car)
# print(cars)

# talabalar = ['hasan', 'olim', 'kozim', 'ali']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba}ning bahosini kiriting>> ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = int(baho)
    
# AMALIYOT

# 1. Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir 
# qabul qilib, yangi ro'yxatga joylang.
print("Buyurtma qabul qiluvchi dastur ")

maxsulotlar = []
ishora = True
n = 1
while ishora:
    buyurtma = input(f"{n}-Maxsulot nomini kiriting:>> ")    
    maxsulotlar.append(buyurtma)
    takror = input("yana davom etasizmi? ha/yo'q ")
    if takror == "yo'q":
        break
    n += 1

# 2. e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
# 3. Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni 
# e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot 
# e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.

# JAVOBLAR