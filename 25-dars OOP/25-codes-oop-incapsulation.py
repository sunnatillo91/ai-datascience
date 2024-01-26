# -*- coding: utf-8 -*-
"""
25-DARS OOP Incapsulation

Created on Thu Jan 25 21:00:43 2024

@author: Sunnatillo
"""

from avto import Avto
            
avto1 = Avto("GM", "Malibu", "Qora", 2023, 30000, 100)
avto2 = Avto("GM", "Lacetti", "Oq", 2023, 20000, 200)
avto3 = Avto("GM", "Cobalt", "Qora", 2023, 15000, 150)
print(avto1.get_km())
print(avto1.get_num_avto())

# AMALIYOT
# Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga yopiq xususiyatlar 
# qo'shing va ularning qiymatini ko'rsatuvchi va o'zgartiruvchi metodlar yozing.
class Shaxs:
    odamlar_soni = 0
    def __init__(self, ism, familiya, tyil, pasport):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.__pasport = pasport
        Shaxs.odamlar_soni += 1
        
    @classmethod
    def get_odamlar_soni(cls):
        return cls.odamlar_soni
    
    def get_info(self):
        info = f"{self.ism} {self.familiya}"
        return info
    
    def get_pasport(self):
        return self.__pasport
    
    def change_pasport(self, new_pasport):
        self.__pasport = new_pasport
        return self.__pasport

person = Shaxs("Alijon", "Valiyev. ", 1995, 'AD12345')
# print(person.get_pasport())
# print(person.change_pasport("AD3566545"))

class Talaba(Shaxs): # Shaxs-super klas, Talaba-voris klas
    """Talaba klasi"""
    __talabalar_soni = 0 # clasga oid xususiyatlarni ham incapsulyatsiya orqali yashirsa bo'ladi
    def __init__(self, ism, familiya, tyil, pasport, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, tyil, pasport)
        self.__idraqam = idraqam
        self.bosqich = 1
        Talaba.__talabalar_soni += 1

    @classmethod
    def get_talabalar_soni(cls):
        return cls.__talabalar_soni
        
    def get_id(self):
        return self.__idraqam     
    
    def change_id(self, new_id):
        self.__idraqam = new_id
        return self.__idraqam
    
    def get_info(self): # bu metodni qaytadan talaba uchun yozdik mana shu holat polymorphism
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya} "
        info += f"{self.bosqich}-bosqich talabasi. ID: {self.idraqam}"
        return info
    
talaba = Talaba("Valijon", "Hakimov", "AB456554", 2001, "AD123221")
print(talaba.get_id())
print(talaba.change_id("ID321456"))

# Yuqoridagi klasslarga talabalar_soni va odamlar_soni degan klassga oid xususiyatlar qo'shing.


# Klassga oid xususiyatlar bilan ishlash uchun maxsus @classmethod lar yozing 