# -*- coding: utf-8 -*-
"""
09-Dars  FOR LOOP
Created on Fri Dec 22 19:58:53 2023

@author: Sunnatillo
"""

mehmonlar = ["Ali", "Vali", "Hasan", "Husan", "OLim"]
for mehmon in mehmonlar:
    print("Salom", mehmon)
    
mehmonlar = ["Ali", "Vali", "Hasan", "Husan", "OLim"]
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 25-dekabr kuni nahorga oshga taklif qilamiz")
    print("Hurmat bilan, Ochilovlar oilasi\n")

sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")

sonlar = list(range(11))  # 1 dan 10 gacha sonlar ro'yxatini shakllantiramiz
sonlar_kvadrati = []  # bo'sh ro'yxat yaratamiz
for son in sonlar:    #  sonlardagi har bir son uchun 
    sonlar_kvadrati.append(son**2)    # uning kvadratini hisoblab konsolga chiqaramiz
    
print(sonlar)
print(sonlar_kvadrati) 

dostlar = []
print("5 ta eng yaqin do'stingizni kim?")
for n in range(5):
    dostlar.append(input(f"{n+1}-do'stingizni ismini kiriting >>>"))
print(dostlar)

# AMALIYOT
# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
ismlar = ["Olim", "Salim", "Karim", "Jahon", "Baxrom"]
for ism in ismlar:
    print("Salom", ism)

# # Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
print(f"Kod {len(ismlar)} marta takrorlandi")
# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
toq_sonlar = list(range(11,100,2))
for toq_son in toq_sonlar:
    print(toq_son**3)
# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. 
# Natijani konsolga chiqaring.
kinolar = []
print("5 ta eng yoqtirgan kinolaringiz qaysi? ")
for kino in range(5):
    kinolar.append(input(f"{kino+1}- kino nomini kiriting >>> "))
print(kinolar)

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan 
# odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
nechta_odam = int(input("Bugun nechta odam bilan suhbatlashdingiz?>>> "))
suhbatdoshlar = []
# print(nechta_odam)
for suhbatdosh in range(nechta_odam):
    suhbatdoshlar.append(input(f"{suhbatdosh+1}-suhbatdoshingizni kiriting>>> "))
print(suhbatdoshlar)

