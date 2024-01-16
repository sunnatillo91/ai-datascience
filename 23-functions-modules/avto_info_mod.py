# -*- coding: utf-8 -*-
"""
23-dars: MODULLAR

Created on Tue Jan 16 18:37:02 2024

@author: Sunnatillo
"""
 
def avto_info(kompaniya, model, rangi, korobka, yili, narxi = None):
    avto = {
        'kompaniya':kompaniya,
        'model':model,
        'rangi':rangi,
        'korobka':korobka,
        'yili':yili,
        'narxi':narxi
        }
    return avto

def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta qilib chiqaradi"""
    avtolar = []
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting: ", end='')
        kompaniya = input("Ishlab chiqaruvchi: ")
        model=input('Modeli: ')
        rangi=input('Rangi: ')
        korobka=input('Korobka: ')
        yili=input('Ishlab chiqarilgan yili: ')
        narxi=input('Narxi: ')
        #Foydalanuvchi kiritgan ma'lumotlrdan avto_info yordamida
        #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz
        avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narxi))
        #Yana avto qo'shish qo'shmaslikni so'raymiz
        javob=input("Yana avto qo'shasizmi? (yes/no) ")
        if javob == 'no':
            break
    return avtolar

def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rangi'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yili']}-yil, {avto_info['narxi']}$ ")
    
avto1 = avto_info('GM', 'Malibu', "Qora", 'avtomat', 2022, 35000)
info_print(avto1)

