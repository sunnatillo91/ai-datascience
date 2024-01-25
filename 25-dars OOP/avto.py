# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 21:35:28 2024

@author: Sunnatillo
"""

from uuid import uuid4

# INCAPSULATION 
 
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
        self.__id = uuid4()  # bu qiymatlarga maxsus metodlar yordamidagina murojaat qilish mumkin
        Avto.__num_avto += 1  # Avto klasidan necha marta foydalanilganini hisoblaydi
        
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto    
    def get_km(self):
        return self.__km
        
    def get_id(self):
        return self.__id
    
    def add_km(self, km):
        """Mashinaning km ga yana km qo'shish"""
        if km>=0:
            self.__km += km
        else:
            print("Mashina km ini kamaytirib bo'lmaydi")