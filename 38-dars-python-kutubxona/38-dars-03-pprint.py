# -*- coding: utf-8 -*-
"""
38-DARS Python standart kutubxonasi

Created on Tue Feb  6 18:08:54 2024

@author: Sunnatillo
"""

from pprint import pprint
import json

filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)
    
pprint(bemor)  # bu f-ya ma'lumotni chiroyliroq qilib chiqarib beradi
print(bemor)