# -*- coding: utf-8 -*-
"""
38-DARS Python standart kutubxonasi

Created on Mon Feb  5 20:08:32 2024

@author: Sunnatillo
"""

# https://docs.python.org/3/library/

import datetime as dt

# datetime()
# hozir = dt.datetime.now()
# print(hozir)
# # sanani ajratib olish
# print(hozir.date())
# # soatni ajratib olish
# print(hozir.hour)
# # minutni ajratib olish
# print(hozir.minute)
# # sekundni ajratib olish
# print(hozir.second)

# date()
bugun = dt.date.today()
print(f"Bugungi sana: {bugun}") 
ertaga = dt.date(2024,2,6)
print(f"Ertangi sana: {ertaga}")

# time()
hozir = dt.datetime.now()
ayni_vaqt = hozir.time()
print(f"Ayni vaqt: {ayni_vaqt}")
vaqtKeyin = dt.time(21,18,12)

# Sanalar orasidagi farq
bugun = dt.date.today()
ramazon = dt.date(2024, 3, 10)
farq = ramazon-bugun
print(f"Ramazonga nasib etsa {farq.days} kun qoldi")