# -*- coding: utf-8 -*-
"""
24-DARS LAMBDA  nomsiz funksiya map()

Created on Wed Jan 17 19:15:43 2024

@author: Sunnatillo
"""

from math import sqrt

# map() yordamida kamroq kod yozib kerakli natijaga erishildi
# sonlar = list(range(17))
# # ildizlar = list(map(sqrt, sonlar))   #map() funksiyasi f-ya va ro'yxat qabul qilib obyekt qaytaradi
# # print(ildizlar)

# # sonlar = list(range(17))
# # ildizlar = []
# # for son in sonlar:
# #     ildizlar.append(sqrt(son))
# # print(ildizlar)

# # Bir xil misolning bir necha usuli (1-usul)
# def daraja2(x):
#     """Berilgan sonning kvadratini qaytaruvchi f-ya"""
#     return x*x
# print(list(map(daraja2, sonlar)))

# # (2-usul)
# # lambda va map() yordamida qisqa kod yozib kerakli natijaga erishildi
# kvadratlar = list(map(lambda x:x*x, sonlar))
# print(kvadratlar)

# # (3-usul)
# kvadratlar = []
# for son in sonlar:
#     kvadratlar.append(son*son)
# print(kvadratlar)

a = [4,5,6]
b = [7,8,9]
a_plus_b = list(map(lambda x,y:x+y, a,b))
print(a_plus_b)
