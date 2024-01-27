# -*- coding: utf-8 -*-
"""
25-codes-Dunder Metodlar (Double under score)

Created on Sat Jan 27 09:49:42 2024

@author: Sunnatillo
"""

class Avto:
    """Avtomobil klassi"""
    __num_avto = 0  # bu klasga xos xususiyat
    def __init__(self, make, model, rang, yil, narx, km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km  # pastki __ chiziqlar yordamida mashina km i ko'rinmaydigan qilindi
        Avto.__num_avto += 1  # Avto klasidan necha marta foydalanilganini hisoblaydi
        
    # def __str__(self):
    #     return f"Avto: {self.make} {self.model}"
    
    def __repr__(self):  # repr metodi str kabi vazifa bajaradi, str dan ko'proq f-ya b-n ishlaydi
        return f"Avto: {self.make} {self.model}"
    
    def __eq__(self, y):    # 2 ta obyektning tegligini tekshiradi
        return self.narx == y.narx
    
    def __lt__(self, y):     # 2 ta obyektning katta yoki kichikligini tekshiradi. lt - lower than
        return self.narx < y.narx 
    
    def __le__(self, y):
        return self.narx <= y.narx
    
class Avtosalon:
    """Avtosalon klassi"""
    def __init__(self, name):
        self.name = name
        self.avtolar = []
        
    def __repr__(self):  # repr metodi str kabi vazifa bajaradi, str dan ko'proq f-ya b-n ishlaydi
        return f"Avtosalon: {self.name}"
    
    def __getitem__(self, index):
        return self.avtolar[index]
    
    def add_avto(self, *qiymat):  # *qiymat orqali istalgancha qiymat berish mumkin
        for avto in qiymat:
            if  isinstance(avto, Avto):  #isinstance obyekt clasga tegishli yoki yo'qligini aniqlaydi
                return self.avtolar.append(avto)
            else:
                print("Avto kiriting")
    
salon1 = Avtosalon("Maxavto")

print(salon1)

avto1 = Avto("Tesla", "TeslaX", "Dark Blue", 2024, 85000)
avto2 = Avto("Lamborgini", "Huracan", "Dark Green", 2024, 302000)
salon1.add_avto(avto1, avto2)
# print(avto1)