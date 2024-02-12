# -*- coding: utf-8 -*-
"""
36-DARS Funksiyalarni tekshirish, UNITTEST moduli

Created on Wed Jan 31 21:16:56 2024

@author: Sunnatillo
"""

def get_full_name(ism, familiya, otasi = ''):
    if otasi:
        return f"{ism} {familiya} {otasi}".title()
    else:
        return f"{ism} {familiya}".title()

# print(get_full_name('alijon', 'valiyev'))
