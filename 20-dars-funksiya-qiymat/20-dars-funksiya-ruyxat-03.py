# -*- coding: utf-8 -*-
"""
20-dars FUNKSIYADAN QIYMAT QAYTARISH

Created on Wed Jan 10 19:22:53 2024

@author: Sunnatillo
"""
# FUNKSIYADAN RO'YXAT QAYTARISH

def oraliq(min, max, qadam=1):
    sonlar = []
    while min<max:
        sonlar.append(min)
        if qadam:
            min += 2
        else:
            min += 1
    return sonlar
oraliq(0, 10)
print(oraliq(10, 21, 2))
