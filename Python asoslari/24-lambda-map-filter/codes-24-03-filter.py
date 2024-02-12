# -*- coding: utf-8 -*-
"""
24-DARS LAMBDA  nomsiz funksiya, filter

Created on Wed Jan 17 19:51:36 2024

@author: Sunnatillo
"""

import random as r

# sonlar = r.sample(range(100), 10) # 0-99 orasidagi tasodifiy sonlarni qaytaradi
# print(sonlar)

# # # Bir xil misolning bir necha usuli (1-usul)
# def juftmi(x):
#     """x juft b-sa True aks holda False qaytaruvchi f-ya"""
#     return x%2 == 0
# juft_sonlar = list(filter(juftmi, sonlar))
# print(juft_sonlar)

# # (2-usul) filter va sonlar yordamida
# juft_sonlar = list(filter(lambda x:x%2 ==0, sonlar))
# print(juft_sonlar)

mevalar = ['olma', 'anor', 'uzum', 'shaftoli', 'tarvuz', 'qovun', 'banan']
harf = 'u'
# mevalar_harf = list(filter(lambda meva:meva.startswith(harf), mevalar))
# print(mevalar_harf)

mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
# print(mevalar2)  # harflari soni 5 tadan kam mevalarni chiqaradi

mevalar3 = list(filter(lambda meva:(meva.startswith('a') or meva.endswith('m')), mevalar))

print(mevalar3)

