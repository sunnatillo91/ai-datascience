# -*- coding: utf-8 -*-
"""
19-dars FUNCTIONS (FUNKSIYALAR)
Created on Tue Jan  9 20:50:27 2024

@author: Sunnatillo
"""
# QOIDA
# O'zgaruvchilarni nomlashda ot funksiyalarni nomlashda esa fe'l qo'llash tavsiya qilinadi

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum")
    
# salom_ber()


def salom_ber(ism):    # bu yerda ism - parametr
    """Foydalanuvchi ismini qabul qilib,   
    unga Salom beruvchi funksiya"""       # DOCSTRING FUNKSIYA haqida ma'lumot 
    print(f"Assalomu alaykum {ism.title()}")
    
salom_ber('olim')   # bu holatda foydalanuvchidan olinayotgan qiymat argument deyiladi

# funksiya haqidagi ma'lumotni konsolga chiqarish uchun print(funksiya.__doc__)
print(salom_ber.__doc__)