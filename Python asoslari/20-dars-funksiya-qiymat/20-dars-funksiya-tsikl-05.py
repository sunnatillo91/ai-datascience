# -*- coding: utf-8 -*-
"""
20-dars FUNKSIYADAN QIYMAT QAYTARISH

Created on Wed Jan 10 19:53:16 2024

@author: Sunnatillo
"""
# FUNKSIYA VA TSIKL

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

print("Saytimizdagi avtolar ro'yxatini shakllantiramiz")
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
print("Salonimizdagi avtolar")
for avto in avtolar:
    if avto['narxi']:
        narxi = avto['narxi']
    else:
        narxi = 'Noma\'lum'
    print(f"{avto['rangi'].title()} {avto['model'].title()} narxi {narxi}")
    
    