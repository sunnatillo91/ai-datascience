# -*- coding: utf-8 -*-
"""
27-DARS Fayllar bilan ishlash (Writing pickle)

Created on Mon Jan 29 16:54:21 2024

@author: Sunnatillo
"""

import pickle

# O'ZGARUVCHILARNI SAQLASH

# Adashib ketmaslik uchun, alohida o'zgaruvchilarni alohida fayllarga saqlash 
# tavsiya qilinadi.

talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2005, 'kurs':2}
talaba2 = {'ism':'Olim', 'familiya':'Jurayev', 'tyil':2001, 'kurs':4}

with open('info.pkl', 'wb') as file:  # wb - write binary ikkilik sanoq sistemasida yozish
    pickle.dump(talaba1, file)
    pickle.dump(talaba2, file)
    
    