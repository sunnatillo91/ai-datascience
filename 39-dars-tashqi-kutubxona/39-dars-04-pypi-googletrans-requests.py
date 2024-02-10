# -*- coding: utf-8 -*-
"""
39-DARS PYTHON TASHQI KUTUBXONASI Googletranslate requests

Created on Sat Feb 10 10:05:26 2024

@author: Sunnatillo
"""

import googletrans
import requests

url = "https://api.adviceslip.com/advice"
r = requests.get(url)
advice = r.json()['slip']['advice']
print(advice)

translator = googletrans.Translator()
tarjima = translator.translate(advice, dest='uz')
print(tarjima.text)