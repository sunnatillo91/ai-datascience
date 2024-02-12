# -*- coding: utf-8 -*-
"""
39-DARS PYTHON TASHQI KUTUBXONASI BeautifulSoup

Created on Sat Feb 10 10:19:45 2024

@author: Sunnatillo
"""

import requests
from bs4 import BeautifulSoup

sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
news = soup.find_all(class_='news-title')
print(news[0].text) # kun.uz asosiy sahifasidagi 1-yangilik
print(news) # kun.uz asosiy sahifasidagi yangiliklar
