# -*- coding: utf-8 -*-
"""
26-DARS Xatolar bilan ishlash. except ni afzalligi dastur to'xtab qolmaydi

Created on Sat Jan 27 17:16:54 2024

@author: Sunnatillo
"""
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except:
#     print("Siz butun son kiritmadingiz")
# else:
#     print(f"Siz {2024-yosh}-yilda tug'ilgansiz")

# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Siz butun son kiritmadingiz")
# else:
#     print(f"Siz {2024-yosh}-yilda tug'ilgansiz")

# ZeroDivisionError
# x, y = 5, 10
# try:
#     x/(x-5)
# except:
#     print("0 ga bo'lish mumkin emas")

#IndexError
# mevalar = ['olma', 'uzum', 'anor', 'nok', 'behi']
# try:
#     print(mevalar[5])
# except IndexError:
#     print(f"Sizda bor yo'g'i {len(mevalar)} ta meva bor")

#KeyError
user = {
        "username":"sunnatillo",
        "status":"admin",
        'email':'sunnatillo@gmail.com',
        "phone":'992372448'       
        }
key = 'tel'
try:
    print(f"Foydalanuvchi: {user[key]}")
except KeyError: 
    print("Bunday kalit mavjud emas")
print(user['username'])
    
# FileNotFoundError
filename = "data.txt"
try:
    with open(filename) as f:
        text = f.read()
except FileNotFoundError:
     print(f"{filename} mavjud emas")