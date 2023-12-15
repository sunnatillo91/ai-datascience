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

# ism = 'Ahad'
# familiya = 'Qayum'
# print(ism + ' ' + familiya) # ikki o'zgaruvchi orasiga bo'sh joy qo'shamiz

# ism = "Ahad"
# familiya = 'Qayum'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif)

# Maxsus belgilar

# print('Hello world')
# print('Hello \tworld')  #Hello 	world
# print('Hello \nworld!')

# STRING METODLARI

# ism = 'Muhammad'
# familya = ' ibn Abdulloh'
# ism_sharif = f"{ism} {familya}"
# print(ism_sharif.upper())
# # Agar o'zgaruvchini o'zini o'zgartirmoqchi bo'lsak quyidagicha ko'rinishda bo'ladi
# ism_sharif = ism_sharif.upper()
# print(ism_sharif.lower())
# print(ism_sharif.title())
# print(ism_sharif.capitalize())

# meva = '     olma      '
# print('Men' + meva.lstrip(), ' sotib oldim')
# print('Men' + meva.rstrip() + ' sotib oldim')
# print('Men', meva.strip()+ ' sotib oldim')

# ism = input("Ismingiz nima? \n>>>")
# print("Assalomu alaykum "+ ism.title())


# AMALIYOT
# Quyidagi mashqlarni bajaring:

# Quyidagi o'zgaruvchilarni yarating:
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
print(kocha + ' ' + 'ko\'chasi,' + ' ' + mahalla + ' ' + 'mahallasi,' + ' ' + tuman + ' ' + 'tumani,' + ' ' + viloyat + ' ' + 'viloyati')
# Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati

# Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
# kocha = input("Ko'changiz nomi nima? \n>>>")
# mahalla = input("Mahallangiz nomi nima? \n>>>")
# tuman = input("tumaningiz nomi nima? \n>>>")
# viloyat = input("Viloyatingiz nomi nima? \n>>>")
# print(kocha + ' ' + 'ko\'chasi,' + ' \n' + mahalla + ' ' + 'mahallasi,' + ' \n' + tuman + ' ' + 'tumani,' + ' \n' + viloyat + ' ' + 'viloyati')

# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
# print(kocha + ' ' + 'ko\'chasi,' + ' \n' + mahalla + ' ' + 'mahallasi,' + ' \n' + tuman + ' ' + 'tumani,' + ' \n' + viloyat + ' ' + 'viloyati')
# Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
manzil = f"{kocha} ko'chasi,\n{mahalla} mahallasi,\n{tuman} tumani,\n{viloyat} viloyati"

# manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
print(manzil.capitalize())
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
