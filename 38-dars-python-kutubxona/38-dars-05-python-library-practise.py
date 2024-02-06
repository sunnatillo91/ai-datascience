# -*- coding: utf-8 -*-
"""
38-DARS Python standart kutubxonasi Practise

Created on Tue Feb  6 19:27:45 2024

@author: Sunnatillo
"""
import datetime as dt
from datetime import date


# AMALIYOT
# 1. Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqaring

# farq = 0
# i = 0
# while i<10:
#     bugun = dt.date.today()
#     keyingi_kun = bugun + dt.timedelta(farq)
#     print(f"{i+1}-kun {keyingi_kun}")
#     farq += 14
#     i += 1

# 2. Ramazon va qurbon hayitigacha qolgan kunlarni konsolga chiqaring
# ramazon = dt.date(2024,3,10)
# hayit = dt.date(2024,5,19)
# farq_hayit = hayit-bugun
# farq = ramazon-bugun
# print(f"Ramazongacha {farq.days} kun qoldi")
# print(f"Hayitgacha {farq_hayit.days} kun qoldi")

# 3. Tug'ilgan kuningizdan bugungi sanagacha qancha yil, oy, kun o'tganini qaytaruvchi 
# funksiya yozing
bugun = date.today()
# bugun = date.year
tyil = dt.date(1991,6,20)
farq_days = bugun-tyil
d = date().fromordinal(farq_days.days)
# yil = farq_days.date.year()
print(d)
# 4. Foydalanuvchidan telefon raqamini kiritishni so'rang. Kiritlgan qiymatni andoza yordamida 
# tekshiring

# 5. Berilgan matndan veb sahifa manzilini ajratib olyuvchi funksiya yozing. Quyidagi matndan 
# namuna sifatida foydalanishingiz mumkin: