# -*- coding: utf-8 -*-
"""
25-DARS OOP Inheritance (Vorislik) and Polymorphism

Created on Wed Jan 24 20:57:03 2024

@author: Sunnatillo
"""

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self, ism, familiya, pasport, tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.pasport = pasport
        self.tyil = tyil
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya} "
        info += f"Pasport: {self.pasport}, {self.tyil}-yilda tug'ilgan"
        return info
    
    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi f-ya(metod)"""
        age = yil-self.tyil
        return age
person = Shaxs("Alijon", "Valiyev. ", 'AD12345', 1995)
person.get_age(2024)
person.get_info()

class Talaba(Shaxs): # Shaxs-super klas, Talaba-voris klas
    """Talaba klasi"""
    def __init__(self, ism, familiya, pasport, tyil, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, pasport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        
    def get_id(self):
        return self.idraqam                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        
        
talaba = Talaba("Valijon", "Hakimov", "AB456554", 2001, "AD123221")
# talaba.get_info()  # get_info() metodi ham vorislik orqali o'tdi
        
# Polymorphism
class Talaba(Shaxs): # Shaxs-super klas, Talaba-voris klas
    """Talaba klasi"""
    def __init__(self, ism, familiya, pasport, tyil, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, pasport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        
    def get_id(self):
        return self.idraqam     
    
    def get_info(self): # bu metodni qaytadan talaba uchun yozdik mana shu holat polymorphism
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya} "
        info += f"{self.bosqich}-bosqich talabasi. ID: {self.idraqam}"
        return info
talaba = Talaba("Valijon", "Hakimov", "AB456554", 2001, "AD123221")
talaba.get_info()

        
         
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        