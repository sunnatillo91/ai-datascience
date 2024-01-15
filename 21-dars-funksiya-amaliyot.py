# -*- coding: utf-8 -*-
"""
21-dars amaliyot

Created on Mon Jan 15 18:11:19 2024

@author: Sunnatillo
"""
# AMALIYOT
# - Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga 
# o'zgatiruvchi funksiya yozing. 
ismlar = ['ali', 'vali', 'hasan', 'husan']
# def katta_harf(ismlar):
#     talabalar = []
#     while ismlar:
#         for ism in ismlar:
#             ism = ismlar.pop()
#             talabalar.append(ism.title())
#     return talabalar
    
# talabalar = katta_harf(ismlar)
# print(talabalar)
# Yuqoridagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qilib o'zgartiring
# def katta_harf(ismlar):
#     talabalar = []
#     for ism in ismlar[:]:
#         talabalar.append(ism.title())
#     return talabalar

# talabalar = katta_harf(ismlar)
# print(talabalar)
# print(ismlar)

# Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan va asl ro'yxatga 
# o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting:>> ")
        baholar[ism.title()] = int(baho)
    return baholar
talabalar_baholari = bahola(ismlar)
print(talabalar_baholari)
print(ismlar)


