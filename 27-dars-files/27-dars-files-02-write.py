# -*- coding: utf-8 -*-
"""
27-DARS Fayllar bilan ishlash (Writing)

Created on Mon Jan 29 16:33:21 2024

@author: Sunnatillo
"""
# Yangi fayl yaratish

faylnomi = "new_file.txt"  # Eslatma faylnomi tanlashda yangi no qo'yish kerak. 
# Agar o'xshash nom qo'yilsa eski fayl o'chirilib o'rniga yangi ma'lumot yoziladi
ism = 'olimjon hasanov'
tyil = 1998
with open(faylnomi, 'w') as fayl:
    fayl.write(ism+'\n')
    fayl.write(str(tyil)+'\n')
    
# Mavjud faylga qo'shimcha qilish

with open(faylnomi, 'a') as fayl:
    fayl.write('Alijon Valiyev\n')
    fayl.write('2000')
    