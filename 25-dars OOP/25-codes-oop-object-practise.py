# -*- coding: utf-8 -*-
"""
25-DARS OOP obyektlar bilan ishlash AMALIYOT

Created on Tue Jan 23 21:50:18 2024

@author: Sunnatillo
"""

# AMALIYOT
# 1. Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta 
# xususiyatlar (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga 
# standart qiymat bering (masalan, kilometer=0)
class Avto:
    def __init__(self, model, rang, korobka, narh, yil, kilometr = 3):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.yil = yil
        self.kilometr = kilometr

# 2. Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
# get_info() metodi avto haqida to'liq ma'lumotni matn ko'rinishida qaytarsin
    def get_info(self):
        return f"{self.korobka} korobka {self.rang} {self.model} narxi - {self.narh} $. Ishlab chiqarilgan yili \
{self.yil}, {self.kilometr} km yurgan"
            

# 3. Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
# update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini 
# yangilab borsin
    def update_km(self, km):
        new_km = self.kilometr
        new_km += km
        return new_km 
# 4. Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring 
# (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)

class Avtosalon:
    def __init__(self, nomi, manzili, avtomobillar, telefoni):
        self.nomi = nomi
        self.manzili = manzili
        self.avtomobillar = []
        self.telefoni = telefoni
        
# 5. Avtosalonga yangi avtomobillar qo'shish uchun metod yozing
# Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing
    def avto_qush(self, avto):
        self avtomobillar.append(avto)
        
        
# 6. Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring

# 7. dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va Pythondagi turli 
# klass va obyektlarning xususiyatlari va metodlarini toping (dir(str), dir(int) va hokazo)

avto1 = Avto("Malibu", "Oq", "avtomat", 35000, 2023)
print(avto1.get_info())