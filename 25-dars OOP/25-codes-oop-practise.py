# -*- coding: utf-8 -*-
"""

25-dars OOP KLASSLAR

Created on Mon Jan 22 21:34:11 2024

@author: Sunnatillo
"""

# AMALIYOT
# Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari sifatida 
# odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, 
# email, va hokazo)
# Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi haqida 
# yig'ilgan ma'lumotlarni chiroyli qilib chiqarsin (masalan: "Foydalanuvchi: alijon1994, 
# ismi: Alijon Valiyev, email: alijon1994@gmail.com).
# Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling.

class User:
    def __init__(self, ism, familiya, foydalanuvchi_ismi, email):
        self.ism = ism
        self.familiya = familiya
        self.foydalanuvchi_ismi = foydalanuvchi_ismi
        self.email = email
        
    def get_name(self):
        return self.ism
    
    def get_info(self):
        return f"Foydalanuvchi: {self.foydalanuvchi_ismi}, ismi: {self.ism} {self.familiya}, email: {self.email} "
    
user = User("Alijon", "Valiyev", "alijon45", "alijon1994@gmail.com")
print(user.get_info())