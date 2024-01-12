# -*- coding: utf-8 -*-
"""
20-dars FUNKSIYADAN QIYMAT QAYTARISH

Created on Wed Jan 10 20:46:28 2024

@author: Sunnatillo
"""

# AMALIYOT
# 1. Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini
#  qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. 
#  Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
# def toliq_ism_info(ism, familiya, tyil, tjoy, manzil, email, tel=None):
#     """Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon 
#     raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya"""
#     toliq_ism = {
#         "ism":ism,
#         "familiya":familiya,
#         "tyil":tyil,
#         "tjoy":tjoy,
#         'email':email,
#         'manzil':manzil,
#         'tel':tel}
#     return toliq_ism
# # talaba = toliq_ism_info('orif', 'shamsiyev', 1986, "nurota", 'navoiy', "orif@gmail.com", 939507999)
# # print(talaba)
# # 2. Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni 
# # shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.
# ishora = True
# mijozlar = []
# while ishora:
#     print("Quyidagi ma'lumotlarni kiriting: ", end='')
#     ism = input('ism: ')
#     familiya = input('familiya: ')
#     tyil = input('tyil:')
#     tjoy = input('tjoy: ')
#     manzil = input('manzil: ')
#     email = input('email: ')
#     tel = input('tel: ')
#     mijozlar.append(toliq_ism_info(ism, familiya, tyil, tjoy, manzil, email, tel))
#     takror = input("Yana ma'lumot qo'shasizmi? (yes/no) ")
#     if takror == 'no':
#         ishora = False
# for mijoz in mijozlar:
#     if mijoz['tel']:
#         tel = mijoz['tel']
#     else:
#         tel = 'noma\'lum'
        
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()} {mijoz['tyil']}-yilda {mijoz['tjoy'].title()} tumanida tug'ilgan, \
#     yoshi {2023-int(mijoz['tyil'])}da. Yashash manzili {mijoz['manzil'].title()}, elektron manzili {mijoz['email']}, telefon raqami \
# {mijoz['tel']}")

# # 3. Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
# def eng_katta(a, b, c):
#     """Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya uchta son qabul qilib, 
#     ulardan eng kattasini qaytaruvchi funksiya"""
#     if a>=b and a>=c:
#         return a
#     elif b>=a and b>=c:
#         return b
#     elif c>=a and c>=b:
#         return c
# sonlar = eng_katta(13, 15, 15)
# print(sonlar)
# # 4. Foydalanuvchidan doiraning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va 
# # yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing
# def doira_full_info(rad):
#     """Foydalanuvchidan doiraning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri 
#     va yuzini lug'at ko'rinishida qaytaruvchi funksiya"""
#     diametr = 2*3.14*rad
#     perimetr = diametr
#     yuza =    3.14*rad**2
#     doira_info = {
#         'rad':rad,
#         'diametr':diametr,
#         'perimetr':perimetr,
#         'yuza':yuza
#         }
#     return doira_info
# doira = doira_full_info(3)
# print(f"Radiusi {doira['rad']} bo'lgan doiraning diametri {doira['diametr']}, yuzasi esa {doira['yuza']} ga teng")

# # 5. Berilgan oraliqdagi [tub sonlar](https://uz.wikipedia.org/wiki/Tub_sonlar_ro%CA%BByxati) ro'yxatini 
# # qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta 
# # musbat sonlar)
# def tub_son_ajrat(min, max):
#     """Berilgan oraliqdagi [tub sonlar] ro'yxatini qaytaruvchi funksiya """
#     tub_sonlar = []
#     for n in range(min, max+1):
#         tub = True
#         if (n == 1):
#             tub = False
#         elif (n == 2):
#             tub = True
#         else:
#             for x in range(2, n):
#                 if (n%x == 0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
#     return tub_sonlar
    
# tub_son = tub_son_ajrat(2, 40)
# print(tub_son_ajrat(2, 40))


# 6. Foydalanuvchidan son qabul qilib, shu son miqdoricha [Fibonachchi ketma-ketligidagi]
# (https://medium.com/@qudratxoja.musayev/fibonachchi-sonlari-va-u-haqida-qiziqarli-faktlar-47000a80264d)
# sonlar ro'yxatni qaytaruvchi funksiya yozing.  **Ta’rif**: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan 
# ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi.  
# `1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...`
# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)        
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar
# print(fibonacci(20))
# JAVOBLAR
def generate_fibonacci(n):
    fib_sequence = []
    a, b = 0, 1

    while a <= n:
        fib_sequence.append(a)
        a, b = b, a + b

    return fib_sequence

generate_fibonacci(15)