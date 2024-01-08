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
    

print("Do'stlaringiz yoshini saqlaymiz")
dostlar = {}
ishora = True
while ishora:
    ism = input("Do'stingiz ismini kiriting: ")
    yosh = input("Do'stingiz yoshini kirititng: ")
    dostlar[ism] = int(yosh)
    takror = input("Yana ma'lumot kiritasizmi? ha/yo'q ")
    if takror == "yo'q":
        break
for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")