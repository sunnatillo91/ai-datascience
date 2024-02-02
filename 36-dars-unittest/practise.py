# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 18:49:08 2024

@author: Sunnatillo
"""

# AMALIYOT
# Quyidagi funksiyalarni yarating, va ularning har biri uchun test dasturlarini yozing:
    
# 1. Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya
def eng_katta(a, b, c):
    """Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya"""
    print("3 ta son kiriting")
    a = int(a)
    b = int(b)
    c = int(c)
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>b and c>a:
        return c
    else:
        return a
    
# 2. Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi 
# harfini katta harfga o'zgatiruvchi funksiya

matn = ['Olim', 'Salim', 'Halim']
def katta_harf(*matn):
    """"Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi 
    harfini katta harfga o'zgatiruvchi funksiya """
    info = f"{matn}".title()
    return info
    
katta_harf(matn)
# 3. Berilgan sonlar ro'yxatidan juft sonlarni ajratib oluvchi funksiya

# 4. Berilgan son Fibonachchi ketma-ketligida uchraydimi (True) yoki yo'q (False) 
# qaytaruvchi funksiya yozing.