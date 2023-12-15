# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 22:21:10 2023

@author: Sunnatillo
Ctrl + 1  comment
"""
# O'zgaruvchilar

ism = 'Abdulloh'
yosh = 25

print(ism, yosh)

# O'zgaruvchilarga nom berishda quyidagi qoidalarga amal qiling:

# O'zgaruvchi nomi harf yoki pastki chiziq (_) bilan boshlanishi kerak
# O'zgaruvchi nomi raqam bilan boshlanishi mumkin emas
# O'zgaruvchi nomida faqatgina lotin alifbosi harflari (A-z), raqamlar (0-9) va pastki chiziq (_) qatnashishi mumkin
# O'zgaruvchi nomida bo'shliq (пробел) bo'lishi mumkin emas
# O'zgaruvchi nomida katta-kichik harflar turlicha talqin qilinadi (ism, ISM, va Ism uchta turli o'zgaruvchi)
# Qo'shimcha qoida sifatida:

# O'zgaruvchi nomini kichik harflar bilan yozing.
# O'zgaruvchi nomida 2 va undan ortiq so'z qatnashsa ularning orasini pastki chiziq (_) bilan ajrating (ism_sharif="Anvar Narzullaev")
# O'zgaruvchiga tushunarli nom bering (y=20 emas yosh=20, d="Korea" emas davlat = "Korea" va hokazo)
# Shuningdek o'zgaruvchilarga Pythonda ishlatiladigan funktsiyalar va maxsus kalit so'zlarning (keywords) nomini bermang. Kalit so'zlar ro'yhatini ko'rish uchun Spyder konsolida avval help() deb yozing va Enter tugmasini bosing. Keyin esa keywords deb kiritib, yana Enter bosing. Marhamat, ekraningizda Pythondagi maxsus kalit so'zlar ro'yhatini ko'ryapsiz:

    # AMALIYOT
    
# Quyidagi mashqlarni bajaring:
# + "Hello World!" matnini yangi o'zgaruvchiga yuklang va print() yordamida konsolga chiqaring
word = "Hello World!"
print(word)
# + xabar deb nomlangan o'zgaruvchiga biror matn yuklang va konsolga chiqaring, keyin esa o'zgaruvchiga yangi qiymat berib uni ham konsolga chiqaring.
xabar = "Avvalgi xabar"
print(xabar)
xabar = 'Yangi xabar'
print(xabar)
# + class den nomlangan o'zgaruvchi yarating, unga biror qiymat bering va konsolga chiqaring (siz kutgan natija chiqdimi?)
class = 12:
    print(class)
# Quyidagi kodni bajaring:
    
radius = 5
pi = 3.14159
aylana_yuzi = pi * radius**2
print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)