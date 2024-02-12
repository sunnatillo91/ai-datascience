# -*- coding: utf-8 -*-
"""
39-DARS PYTHON TASHQI KUTUBXONASI Requests

Created on Fri Feb  9 21:34:50 2024

@author: Sunnatillo
"""

import requests
from pprint import pprint

# manzil= "https://kun.uz/news/main"
# r = requests.get(manzil)
# pprint(r.text)

# restcountries API
country = "Russia"
url = f"https://restcountries.com/v3.1/independent?status=true&fields=languages,capital"
r = requests.get(url)
r_json = r.json()[0]
print(r_json)