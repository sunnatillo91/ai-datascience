# -*- coding: utf-8 -*-
"""
23-dars: MODULLAR

Created on Tue Jan 16 21:18:17 2024

@author: Sunnatillo
"""

import random as r

# randint(a, b)
# son = r.randint(0, 100)   # randint(a,b) berilgan oraliqdagi tasodifiy sonlarni qaytaradi
# print(son)

# # choice()
# ismlar = ['olim', 'salim', 'kozim', 'umar']
# ism = r.choice(ismlar)  # ro'yxatni ichidan tasodifiy ism qaytaradi
# print(ism)
# print(r.choice(ism))    # ismni ichidan tasodifiy harf qaytaradi
x = list(range(0,51,5))  # 0dan 50 gacha 5 qadamlik ro'yxat
print(x)
print(r.choice(x))      # ro'yxat ichidan tasodifiy son qaytaradi

# shuffle()
x = list(range(11))
print(x)
r.shuffle(x)    # ro'yxat tartibini tasodifiy o'zgartiradi
print(x)