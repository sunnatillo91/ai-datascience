# -*- coding: utf-8 -*-
"""
06-dars INTEGER SONLAR BILAN ISHLASH

Created on Fri Dec 15 21:10:52 2023

@author: Sunnatillo
"""

# a = 25
# b = 4.2
# pi = 3.14
# temp = 36.6
# # print(type(temp))
# aholi_soni = 7_596_656_345
# print('Aholi soni', aholi_soni)

# x,y,z = 10, 25, 36.6

# c = a*b
# print(c)  # 105.0

# d = 100/2   # natija 50.0
# d = 100//2   # natija 50

# print(d)    

# KONSTANTA
# radius = 5
# PI = 3.14159
# print('Aylana uzunligi=', 2*PI*radius)

# ism = 'Jobir'
# yosh = 33
# xabar = ism + ' ' + str(yosh) + ' ' + 'yoshda'     # string va int ni qo'shib bo'lmasligi sababli str(yosh) f-yadan foydalanamiz
# print(xabar)

# t_yil = int(input("Tug'ilgan yilingizni kiriting >>>"))
# yosh = 2023 - t_yil
# print("Siz ", yosh, " yoshda ekansiz")

a = int("10")
b = float("10")
c = str(36.6)

# AMALIYOT
# Quyidagi dasturlarning har birini alohida fayl ko'rinishida yozing va bajaring:

# Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
# son = int(input("Istalgan son kiriting>>>"))
# print("Sonning kvadrati ", son**2, " ga teng" )
# print("Sonning kubi ", son**3, " ga teng" )

# yosh = int(input("Yoshingizni kiriting >>>"))
# t_yil = 2023-yosh
# print("Siz ", t_yil, " da tug'ilgansiz")

son1 = int(input("Birinchi sonni kiriting >>>"))
son2 = int(input("Ikkinchi sonni kiriting >>>"))

print(f"{son1}+{son2}=", son1+son2)
print(f"{son1}-{son2}=", son1-son2)
print(f"{son1}*{son2}=", son1*son2)
print(f"{son1}/{son2}=", son1/son2)
