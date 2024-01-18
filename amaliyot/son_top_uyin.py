# -*- coding: utf-8 -*-
"""
"SON TOPISH O'YINI"

Created on Wed Jan 17 21:06:59 2024

@author: Sunnatillo
"""

import random

# a = range(11)
# sonlar = []
# def oraliq(min, max):
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar

# 
# if son
# i = 0
# sonlar = range(11)
# for son in sonlar:
#     while x == son:
#         if son < x:
#             print("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling")
#             continue
#         if son > x:
#             print("Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling")
#             continue
#         if son == x:
#             print(f"To'g'ri topdingiz {son} ni o'ylagandim")
#             break
#         i += 1
#     print(son)
    
def son_top(x):
    tasodifiy_son = random.randint(1,x)
    print(f"1 dan {x} gacha son o'yladim topa olasizmi?: ")
    i = 0
    while True:
        i += 1
        taxmin = int(input('>>> '))
        if taxmin < tasodifiy_son:
            print("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling")
        if taxmin > tasodifiy_son:
            print("Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling")
        else:
            break
    
    print(f"To'g'ri topdingiz {taxmin} ni o'ylagandim "    
        f"Siz {i} ta urinishda topdingiz")
    return i

# print(son_top(10))

def son_top_pc(y):
    tasodifiy_son = random.randint(1,y)
    print(f"1 dan {y} gacha son o'ylang. Men topishga urinib ko'raman ")
    i = 0
    while True:
        i += 1
        taxmin = input('>>> ')
        if taxmin == '+':
            print(f"{tasodifiy_son}ni o'yladingiz to'g'ri (t), men o'ylagan son bundan kattaroq(+), yoki kichikroq (-)")
        if taxmin == '-':
            print(f"{tasodifiy_son}ni o'yladingiz to'g'ri (t), men o'ylagan son bundan kattaroq(+), yoki kichikroq (-)")
        else:
            break
    
    print(f"To'g'ri topdim, {i} ta urinishda topdim")
    return i

print(son_top_pc(10))










