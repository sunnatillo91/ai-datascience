# -*- coding: utf-8 -*-
"""
21-DARS. FUNKSIYA VA RO'YXAT

Created on Fri Jan 12 19:21:08 2024

@author: Sunnatillo
"""

def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting:>> ")
        baholar[ism] = int(baho)
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']

baholar = bahola(talabalar)   # bu yerda ro'yxatni asli ishlatildi
baholar = bahola(talabalar[:])  #bunisida esa talabalar ro'yxatidan nusxa olindi
print(baholar)

# AMALIYOT
# - Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga
#  o'zgatiruvchi funksiya yozing. 


def matn(ruyxat):
    matnlar = []
    while ruyxat:
        gap = ruyxat.pop()
        matnlar.append(gap.title())
    return matnlar
print(matn(talabalar[:]))

# Yuqoridagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qilib o'zgartiring

def matn(ruyxat):
    matnlar = []
    for gap in ruyxat:
        matnlar.append(gap.title())
    return matnlar
print(talabalar)
print(matn(talabalar))

# Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan va asl ro'yxatga 
# o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting:>> ")
        baholar[ism] = int(baho)
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
print(bahola(talabalar))

