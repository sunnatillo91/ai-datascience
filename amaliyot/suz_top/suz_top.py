# -*- coding: utf-8 -*-
"""
26-DARS "SO'Z TOP" O'YINI

Created on Sat Jan 20 11:19:46 2024

@author: Sunnatillo
"""

import random
from new_words import words
# from uzwords import words
# print(words)

# print(random.choice(words))
# ism = 
def get_name():
    name = random.choice(words)
    while "-" in name or ' ' in name:
        name = random.choice(words)
    return name.upper()
# get_name()

def display(user_letters,name):
    display_letter = ""
    for letter in name:
        if letter in user_letters:
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter
    
def play():
    name = get_name()
    word_letters = set(name) # so'zni ichidagi harflar takrorlanmasligi uchun set()dan foydalandik
    user_letters = ''
    print(f"Мен {len(name)} хонали суз уйлaдим топа оласизми? ")
    while word_letters:
        print(display(user_letters,name))
        if user_letters:
            print(f"Шу вактгача киритган харфларингиз: {user_letters}")
            
        letter = input("Харф киритинг>> ").upper()
        if letter in user_letters:
            print("Бу харфни аввал киритгансиз. Бошка харф киритинг ")
            continue
        elif letter in name:
            word_letters.remove(letter)
            print(f"{letter} харфи тугри")
        else:
            print("Бундай харф йук")
        user_letters += letter
    print(f"Tабриклайман, {name} {len(user_letters)} та уринишда топдингиз")
play()

# dastlab 5 xonali so'zlar ajratib olinadi. Keyin, ajratilgan so'zlar ichidan 1 so'z generatsiya qilinadi
# keyin tanlangan so'z harflarga ajratiladi. keyin foydalanuvchidan harf kiritish so'raladi.
# Agar harf ajratilgan so'zdagi harflarga mos kelsa, taxmin_suz ga biriktiriladi, aks holda taxminlar 
# degan bo'sh ro'yxatga biriktiriladi. taxmin_suz ni nechta tsikl (urinish) da topgani chiqariladi
 