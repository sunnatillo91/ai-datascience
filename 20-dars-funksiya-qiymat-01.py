# -*- coding: utf-8 -*-
"""
20-dars FUNKSIYADAN QIYMAT QAYTARISH

Created on Wed Jan 10 18:35:01 2024

@author: Sunnatillo
"""

def toliq_ism_yasa(ism, familiya):
    """Toliq ism qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"    # bu yerda toliq_ism mahalliy o'zgaruvchi (local variable)
    return toliq_ism    # mahalliy o'zgaruvchidan funksiyadan tashqarida foydalanib bo'lmaydi

talaba1 = toliq_ism_yasa('olim', 'salimov')
talaba2 = toliq_ism_yasa("salim", 'olimov')
print(f"Darsga kelmagan talabalar: {talaba1.title()} va {talaba2.title}")
print(f"Darsga kechikkan talaba: {talaba2.title()}")
