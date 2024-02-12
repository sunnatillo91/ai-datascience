# -*- coding: utf-8 -*-
"""
25-dars OOP KLASSLAR

Created on Mon Jan 22 20:46:02 2024

@author: Sunnatillo
"""

class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        
    def tanishtir(self):
        return f"Ismim {self.ism} {self.familiya}, tug'ilgan yilim {self.tyil}"
    
    def get_name(self):
        return self.ism
    
    def get_last_name(self):
        return self.familiya
    
    def get_age(self, yil):
        return yil - self.tyil
        
talaba1 = Talaba("Olim", "Salimov", 2001)
talaba2 = Talaba("Husan", "Hasanov", 1978)
print(f"{talaba2.get_name()}")
print(f"{talaba2.get_age(2024)} yoshda")