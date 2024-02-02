# -*- coding: utf-8 -*-
"""
22-DARS: *args (arguments) va **kwargs (keywords arguments)

Created on Mon Jan 15 20:39:09 2024

@author: Sunnatillo
"""

def avto_info(kompaniya, model, **malumotlar):  # 2 ta yulduzcha qo'yilgani uchun istalgancha argument berish mumkin
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar

avto1 = avto_info("GM", "Cobalt", rang = 'qora', yil = 2020)
avto2 = avto_info("Kia", 'k5', rang = 'oq', yil = 2023, narx = 22000, korobka = 'avtomat')
# print(avto1)
# print(avto2)

# AMALIYOT
# 1. Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
def son_kupaytma(*sonlar):
    """Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya"""
    yigindi = 1
    for son in sonlar:
        # son*son
        yigindi *= son
    return yigindi
print(son_kupaytma(2,5,3,8))

# 2. Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. 
# Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda 
# istalgancha berilishi mumkin bo'lsin.
def talaba_info(ism, familiya, **malumotlar):
    """"Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya"""
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar
talaba1 = talaba_info('sunnatillo', 'xayrullayev', tyil = 1991, millati = 'o\'zbek', dini = 'islom')
print(talaba1)
# JAVOBLAR
## GitHub