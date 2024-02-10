# -*- coding: utf-8 -*-
"""
39-DARS PYTHON TASHQI KUTUBXONASI fuzzy 

Created on Sat Feb 10 11:52:11 2024

@author: Sunnatillo
"""

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

from uzwords import words

# # Ikki so'z o'rtasidagi o'xshashlik fozini topish
# print(fuzz.ratio('salom', 'assalom'))
# print(fuzz.ratio('salom', 'salim'))

# # Matnlar orasida 3 ta eng o'xshashlarini ajratib olish
# text = 'салом'
# matches = process.extract(text, words, limit=3)
# print(matches)

# Matnlar orasida eng o'xshashini ajratib olish

text = 'талба'
match = process.extractOne(text, words)
print(match)