# -*- coding: utf-8 -*-
"""
27-DARS Fayllar bilan ishlash

Created on Sat Jan 27 18:39:31 2024

@author: Sunnatillo
"""

# file = open('pi.txt')  # fayllarni bu holatda ochish tavsiya qilinmaydi
# PI = file.read()    
# print(PI)
# file.close()

# with open('pi.txt') as file: # fayllarni shu holatda ochish tavsiya qilinadi
#     pi = file.read()
    
# print(pi) # with yordamida file o'qilganda text shaklda qaytaradi

# pi = pi.rstrip()
# pi = pi.replace('\n','')
# pi = float(pi)
# print(pi)

file_name = 'data/talabalar.txt'
with open(file_name) as file:
    talabalar = file.readlines()
print(talabalar)
talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)