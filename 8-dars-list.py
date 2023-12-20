# -*- coding: utf-8 -*-
"""
08-dars  LISTS
Created on Wed Dec 20 21:11:36 2023

@author: Sunnatillo
"""

#Sort ro'yxatni alifbo tartibi bo'yicha tartiblash
cars = ['Bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort()  #ro'yxatni alifbo tartibi bo'yicha tartiblash
# > **Diqqat!** Tartiblashda katta harflar kichik harflardan avval kelishini hisobga oling. Agar matndagi so'zlarning bosh 
# harfi katta-kichik aralash yozilgan bo'lsa, ularni bir ko'rinishga keltirib olish maqsadga muvofiq bo'ladi.
cars.sort(reverse=True)   #ro'yxatni alifboga teskari tartib bo'yicha tartiblash
print(cars)