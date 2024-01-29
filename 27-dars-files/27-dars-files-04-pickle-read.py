# -*- coding: utf-8 -*-
"""
27-DARS Fayllar bilan ishlash (Reading pickle)

Created on Mon Jan 29 18:15:55 2024

@author: Sunnatillo
"""

import pickle

# O'ZGARUVCHILARNI O'QISH

with open('info.pkl', 'rb') as file:  # rb - read binary ikkilik sanoq sistemasida o'qish
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)
    
print(talaba1)