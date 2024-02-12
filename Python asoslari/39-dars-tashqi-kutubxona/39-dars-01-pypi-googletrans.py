# -*- coding: utf-8 -*-
"""
39-DARS PYTHON TASHQI KUTUBXONASI Googletrans

Created on Thu Feb  8 18:39:52 2024

@author: Sunnatillo
"""

# pypi.org - Pythonda eng katta tashqi kutubxona  
# pip install wikipedia
# pip install googletrans2

from googletrans import Translator

tarjimon = Translator()

matn_uz = "Python - dunyodagi eng mashhur dasturlash tili"

# Istalgan matnni ingliz tiliga tarjima qilish uchun translate metodini chaqiramiz
tarjima = tarjimon.translate(matn_uz)
# Original matn
print(tarjima.origin)
# Tarjima
print(tarjima.text)

# Original matn tili
print(tarjima.src)

# Matnni boshqa tillarga tarjima qilish uchun dest parametridan foydalanamiz
tarjima_ru = tarjimon.translate(matn_uz, dest='ru')
tarjima_ar = tarjimon.translate(matn_uz, dest='ar')
print(tarjima_ru.text)
print(tarjima_ar.text)

# Ingliz tilidan tarjima
matn_en = "Tashkent is the capital of Uzbekistan"
tarjima_uz = tarjimon.translate(matn_en, dest='uz')
print(tarjima_uz.text)