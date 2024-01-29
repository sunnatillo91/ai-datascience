# -*- coding: utf-8 -*-
"""
27-DARS Fayllar bilan ishlash (Writing)

Created on Mon Jan 29 16:54:21 2024

@author: Sunnatillo
"""

import pickle

talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2005, 'kurs':2}
talaba2 = {'ism':'Olim', 'familiya':'Jurayev', 'tyil':2001, 'kurs':4}

with open('info.pkl', 'wb') as file:
    pickle.dump(talaba1, file)