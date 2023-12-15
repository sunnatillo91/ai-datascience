# -*- coding: utf-8 -*-
"""
05-dars STRING (MATN)
Created on Thu Dec 14 11:17:06 2023

@author: Sunnatillo
"""

# ism_familya = "Sunnatillo Xayrullayev "
# shahar = 'Karmana'
# viloyat = 'Navoiy'
# symbol = '🌏'
# phone = '📱'

# print('Men ', ism_familya, viloyat, 'viloyati ', shahar, 'shahrida yashayman',)
# print('Men yangi ', phone, 'sotib oldim')
# ism = 'Karim'
# familya = 'Hakimov'
# ism_sharif = f"{ism} {familya}"

# print(f"{ism} {familya}")
# print(ism_sharif)

# ism = 'Muhammad'
# familya = ' ibn Abdulloh'
# print(f"Payg'ambarimizning ismlari {ism}, shariflari {familya}" )

# Maxsus belgilar

# print('Hello world')
# print('Hello \tworld')  #Hello 	world
# print('Hello \nworld!')

# STRING METODLARI

ism = 'Muhammad'
familya = ' ibn Abdulloh'
ism_sharif = f"{ism} {familya}"
print(ism_sharif.upper())
# Agar o'zgaruvchini o'zini o'zgartirmoqchi bo'lsak quyidagicha ko'rinishda bo'ladi
ism_sharif = ism_sharif.upper()
print(ism_sharif.lower())
print(ism_sharif.title())
print(ism_sharif.capitalize())

meva = '     olma      '
print('Men' + meva.lstrip(), ' sotib oldim')
print('Men' + meva.rstrip() + ' sotib oldim')
print('Men', meva.strip()+ ' sotib oldim')

ism = input("Ismingiz nima? \n>>>")
print("Assalomu alaykum "+ ism.title())



