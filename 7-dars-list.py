# -*- coding: utf-8 -*-
"""
07-dars  LIST
Created on Mon Dec 18 21:08:13 2023

@author: Sunnatillo
"""

mevalar = ['olma', 'anor', 'olcha', 'uzum']  #mevalar ro'yxati
narxlar = [200, 1555, 61000, 5665, -45, 36.6]   #narxlar ro'yxati
sonlar = ['bir', 'ikki', 'uch', 4, 5]   #sonlar va aralash matnlar
ismlar = []  #bo'sh ro'yxat

print(mevalar[-1])  #natija uzum
print(mevalar[0])   #natija olma
print(mevalar[0].title())   #natija Olma

mevalar[0] = 'nok'
print(mevalar[0])   #natija nok

mevalar.append('shaftoli')      #mevalar ro'yxati oxiriga shaftoli qo'shildi
mevalar.insert(2, 'banan')   #mevalar ro'yxatida uchinchi o'ringa banan qo'shildi

cars = []
cars.append('Lacetti')
cars.append('Nexia')