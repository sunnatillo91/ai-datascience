# -*- coding: utf-8 -*-
"""
"SON TOPISH O'YINI"

Created on Wed Jan 17 21:06:59 2024

@author: Sunnatillo
"""

import random
    
def son_top(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"1 dan {x} gacha son o'yladim topa olasizmi?: ")
    takror_user = 0
    while True:
        takror_user += 1
        taxmin = int(input('>>> '))
        if taxmin < tasodifiy_son:
            print("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling")
        elif taxmin > tasodifiy_son:
            print("Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling")
        else:
            break
    # return i
    print(f"To'g'ri topdingiz {taxmin} ni o'ylagandim "    
        f"Siz {takror_user} ta urinishda topdingiz")
    return takror_user

# son_top(10)

def son_top_pc(y=10):
    
    input(f"1 dan {y} gacha son o'ylang. Men topishga urinib ko'raman. Istalgan sonni bosing ")
    
    quyi = 1
    yuqori = y
    takror_pc = 0
    while True:
        takror_pc += 1
        if quyi != yuqori:
            tasodifiy_son = random.randint(quyi,yuqori)
        else:
            tasodifiy_son = quyi
        javob = input(f"{tasodifiy_son} ni o'yladingiz to'g'ri (t), men o'ylagan son bundan \
                      kattaroq(+), yoki kichikroq (-) ")
        if javob == '+':
            quyi = tasodifiy_son + 1
        elif javob == '-':
            yuqori == tasodifiy_son - 1
        else:
            break
    
    print(f"Ajoyib, {takror_pc} ta urinishda topdim")
    return takror_pc
# son_top_pc(10)
# print()

def uyin(x=10,y=10):
    takror = True
    while takror:
        takror_user = son_top(x)
        takror_pc = son_top_pc(y)
        
        if takror_pc<takror_user:
            print(f"{takror_pc} ta urinishda topdim va men yutdim")
        elif takror_user<takror_pc:
            print(f"{takror_user} ta urinishda topdingiz va siz yutdingiz")
        takror = input("O'yinni davom ettirishni xohlaysizmi? (yes/no)")
        if takror == 'no':
            takror = False
uyin()





