# -*- coding: utf-8 -*-
"""
39-DARS PYTHON TASHQI KUTUBXONASI Googletrans

Created on Fri Feb  9 21:24:47 2024

@author: Sunnatillo
"""

from googletrans import Translator
tarjimon = Translator()

msg = "Tarjima uchun so'z kiriting (chiqib ketish uchun 'q' deb yozing): "
while True:
    text = input(msg)
    if text == 'q':
        break
    else:
        tarjima = tarjimon.translate(text, src='uz', dest='en')
        print(tarjima.text)