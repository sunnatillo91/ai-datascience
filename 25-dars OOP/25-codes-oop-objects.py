# -*- coding: utf-8 -*-
"""
25-codes OOP Obyektlar bilan ishlash

Created on Tue Jan 23 20:23:42 2024

@author: Sunnatillo
"""
class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
        
    def get_name(self):
        return self.ism
    def get_fullname(self):
        return f"{self.familiya} {self.ism}"
    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich} - talabasi"
        
talaba = Talaba("Alijon", "Valiyev", 1996)
talaba2 = Talaba("Olimjon", "Umarov", 1954)
# print(talaba.bosqich)

class Fan():
    """Fan nomli klass"""
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
        
    def get_info(self):
        """Fan nomini qaytaradi"""
        return self.nomi
        
    def add_student(self, talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
        
    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot"""
        # talabalar = []
        # for talaba in self.talabalar:
        #     talabalar.append(talaba.get_fullname())
        # return talabalar
    # Yuqoridagi 4 qator kod o'rniga shu vazifani bajaradigan 1 qator kod yozamiz
        return [talaba.get_fullname() for talaba in self.talabalar]
    
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith("__") is False]
    
    
matem = Fan("Oliy matematika")
talaba = Talaba("Alijon", "Valiyev", 1996)
talaba2 = Talaba("Olimjon", "Umarov", 1954)
matem.add_student(talaba)
matem.add_student(talaba2)
# print(matem.get_students())


# __dict__ METODI
print(talaba2.__dict__)
print(talaba2.__dict__.keys())
