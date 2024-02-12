# -*- coding: utf-8 -*-
"""
20-dars FUNKSIYADAN QIYMAT QAYTARISH

Created on Wed Jan 10 18:51:01 2024

@author: Sunnatillo
"""

def toliq_ism_yasa(ism, familiya, otasining_ismi=''):  # otasining_ismi bu yerda ixtiyoriy argument
    """Toliq ism qaytaruvchi funksiya"""
    if otasining_ismi:
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"    # bu yerda toliq_ism mahalliy o'zgaruvchi (local variable)
    return toliq_ism.title()    # mahalliy o'zgaruvchidan funksiyadan tashqarida foydalanib bo'lmaydi

talaba1 = toliq_ism_yasa('olim', 'salimov')
talaba2 = toliq_ism_yasa("salim", 'olimov', 'hakimovich')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
print(f"Darsga kechikkan talaba: {talaba2}")

