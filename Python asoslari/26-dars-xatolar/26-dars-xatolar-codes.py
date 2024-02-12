# -*- coding: utf-8 -*-
"""
26-DARS Xatolar bilan ishlash. except ni afzalligi dastur to'xtab qolmaydi

Created on Sat Jan 27 17:16:54 2024

@author: Sunnatillo
"""
yosh = input("Yoshingizni kiriting: ")
try:
    yosh = int(yosh)
except:
    print("Siz butun son kiritmadingiz")
else:
    print(f"Siz {2024-yosh}-yilda tug'ilgansiz")

yosh = input("Yoshingizni kiriting: ")
try:
    yosh = int(yosh)
except ValueError:
    print("Siz butun son kiritmadingiz")
else:
    print(f"Siz {2024-yosh}-yilda tug'ilgansiz")

ZeroDivisionError
x, y = 5, 10
try:
    x/(x-5)
except:
    print("0 ga bo'lish mumkin emas")

IndexError
mevalar = ['olma', 'uzum', 'anor', 'nok', 'behi']
try:
    print(mevalar[5])
except IndexError:
    print(f"Sizda bor yo'g'i {len(mevalar)} ta meva bor")

KeyError
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

import json
files = ['talaba1.json', 'talaba2.json', 'talaba3.json']
for filename in files:
    try:
        with open(filename) as f:
            talaba = json.load(f)
    except FileNotFoundError:
        print(f"{filename} mavjud emas")
        pass
    else:
        print(talaba['ism'])
 
ValueError, ZeroDivisionError
n = input("Butun son kiriting: ")
try:
    n = int(n)
    x = 20/n
except ValueError: # agar foydalanuvchi butun son kiritmasa
    print("Butun son kiritmadingiz")
except ZeroDivisionError: # agar foydalanuvchi 0 kiritsa
    print("0 ga bo'lish mumkin emas")
else:
    print(f"x = {x}")
    
yosh = input("Yoshingizni kiriting: ")
try:
    yosh = int(yosh)
except:
    print("Siz butun son kiritmadingiz")
else:
    print(f"Siz {2024-yosh}-yilda tug'ilgansiz")

# try except xato yuz berganda xatoni ushlash uchun kerak, agar xatoni oldini olish
# zarur bo'lsa while va if dan foydalanish tavsiya qilinadi
while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit(): # foydalanuvchi kiritgan yosh raqammi?
        yosh = int(yosh)
        break
print(f"Siz {2024-yosh}-yilda tug'ilgansiz")