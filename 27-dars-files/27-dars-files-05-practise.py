# -*- coding: utf-8 -*-
"""
27-DARS Fayllar bilan ishlash (Practise)

Created on Mon Jan 29 18:45:13 2024

@author: Sunnatillo
"""
import pickle

# AMALIYOT
# 1. Bugun o'rgangan narsalaringizni matnga yozing va matnni Python yordamida oching
# with open('file_create.txt') as file:
#     new_file = file.read()
#     new_file = new_file.rstrip()
#     new_file = new_file.replace('\n', '')
# # print(new_file)
# # 2. Quyidagi pi_million_digits.txt faylini yuklab oling (faylda   soni nuqtadan so'ng 
# #  million xona aniqlik bilan yozilgan). 
# with open('pi_million_digits.txt') as file:
#     pi = file.read()
#     tyil = '20061991'
#     for yil in pi:
#         if tyil in pi:
#             print(tyil)
#             break
#         else:
#             print("Sizning yilingiz 'pi' tarkibida yo'q")
#             break
# print(pi)
# 3. Sizning tug'ilgan kuningiz  soni tarkibida uchraydimi yoki yo'q ekanligini 
# aniqlovchi funksiya yozing. Misol uchun, tug'ilgan sanangiz 25 Fevral, 2000-yil bo'lsa, 
# 25022000 ketma-ketligi yuqoridagi matnda uchraydimi yo'q toping.

# 4. Fayl ichidagi matnni float ma'lumot turiga o'tkazing va pickle yordamida yangi 
# faylga saqlang.
# with open('pi_million_digits.txt') as file:
#     pi = file.read()
#     pi_numbers = float(file)
    
# with open('pi_numbers.pkl', 'wb') as file:
#     pickle.dump(pi_numbers, file)
    
# 5. Foydalanuvchidan turli hil ma'lumotlarni so'rab, har bir kiritilgan ma'lumotni 
# yangi qatordan faylga yozib boruvchi dastur tuzing. Dastur qayta chaqirilganida 
# yangi ma'lumotlar fayl oxiridan qo'shilib borsin (yangi faylga emas).
def info_dastur():   
    """Foydalanuvchidan turli hil ma'lumotlarni so'rab, har bir kiritilgan ma'lumotni 
     yangi qatordan faylga yozib boruvchi dastur """
    malumot = input("Istalgan ma'lumot kiriting:>> ")
    with open('info.txt', 'a') as file:
       file.write(malumot+'\n')
       return malumot
       
print(info_dastur())