# -*- coding: utf-8 -*-
"""
25-DARS OOP Inheritance Practise 
Created on Thu Jan 25 18:21:21 2024

@author: Sunnatillo
"""

# AMALIYOT
# 1. Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. Bu xususiyat parametr 
# sifatida uzatilmasin va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])
# class Talaba:
#     """Talaba klassi"""
#     def __init__(self, ism, familiya, bosqich, manzil):
#         self.ism = ism
#         self.familiya = familiya
#         self.bosqich = bosqich
#         self.manzil = manzil
#         self.fanlar = []
        
#     def get_info(self):
#         info = f"{self.ism} {self.familiya} {self.bosqich}-bosqich talabasi"
#         return info

# 2. Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.
class Fan:
    """Fan klasi"""
    def __init__(self, nomi):
        """Fan xususiyatlari"""
        self.nomi = nomi
        
    def get_fan(self):
        return self.nomi
matem = Fan("Oliy matematika")
fizika = Fan("Fizika")
en = Fan("Ingliz tili")

# print(matem.get_fan())

# 3. Talaba klassiga fanga_yozil() degan yangi metod yozing. Bu metod parametr sifatida 
# Fan klassiga tegishli obyektlarni qabul qilib olsin va talabaning fanlar ro'yxatiga qo'shib qo'ysin.
class Talaba:
    """Talaba klassi"""
    def __init__(self, ism, familiya, bosqich, manzil):
        self.ism = ism
        self.familiya = familiya
        self.bosqich = bosqich
        self.manzil = manzil
        self.fanlar = []
        
        
    def get_info(self):
        info = f"{self.ism} {self.familiya} {self.bosqich}-bosqich talabasi"
        return info
    
    def fanga_yozil(self, fan):
        self.fanlar.append(fan)
        return self.fanlar
    
    def fanlar(self):
        return f"{self.ism} yozilgan fanlar {self.fanlar}"
    
    def remove_fan(self, fan):   
        if fan in self.fanlar:
            self.fanlar.remove(fan)
            return self.fanlar
        else:
            return "Siz bu fanga yozilmagansiz"
    
talaba1 = Talaba("Olimjon", "Valiyev", 2, 'Samarqand')

talaba1.fanga_yozil(en.get_fan())
talaba1.fanga_yozil(matem.get_fan())
talaba1.fanga_yozil(fizika.get_fan())
talaba1.remove_fan("Ingliz tili")
# print(talaba1.remove_fan("Tarix"))

# 4. Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun remove_fan() metodini yozing. 
# Agar bu metodga ro'yxatda yo'q fan uzatilsa "Siz bu fanga yozilmagansiz" xabarini qaytarsin.


# 5. Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor, 
# Foydalanuvchi, Sotuvchi, Mijoz va hokazo)
class Shaxs:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
    
    def get_info(self):
        info = f"{self.ism} {self.familiya}"
        return info
    
class Seller(Shaxs):
    def __init__(self, ism, familiya, tyil, mahorat):
        super().__init__(ism, familiya, tyil)
        self.mahorat = mahorat
        
    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Mahorati: {self.mahorat}, {self.tyil}-yilda tug'ilgan"
        return info
    
seller1 = Seller("Elyor", "Umarov", 1994, "Kirishimli")
print(seller1.get_info())
    
# 6. Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.
class Professor(Shaxs):
    """Professor klassi"""
    def __init__(self, ism, familiya, tyil, yunalish):
        """Professor xususiyatlari"""
        super().__init__(ism, familiya, tyil)
        self.yunalish = yunalish
        
    def get_prof(self):
        info = f"{self.ism} {self.familiya} "
        info += f"{self.yunalish} yo'nalishida doktorlik dissertatsiya yoqlagan"
        return info
    
    def get_info(self):
        info = f"{self.ism} {self.familiya} {self.tyil}-yilda tug'ilgan. "
        info += f"{self.yunalish} yo'nalishida doktorlik dissertatsiyasini yoqlagan"
        return info

professor1 = Professor("Baxouddin", "Salimov", 1993, "Boyitish")
print(professor1.get_info())

# 7. Barcha yangi klasslar uchun get_info() metodini qayta yozib chiqing.
        
class User(Shaxs):
    """User klassi"""
    def __init__(self, ism, familiya, tyil, jins):
        """Xususiyatlari"""
        super().__init__(ism, familiya, tyil)    
        self.jins = jins
        
    def get_user(self):
        return f"{self.ism} {self.jins}"
    
    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Jinsi: {self.jins}, {self.tyil}-yilda tug'ilgan"
        return info
    
user1 = User("Olim", "Nasimov", 1991, "Erkak")
print(user1.get_info())
    
# 8. Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun Foydalanuvchi klassidan 
# Admin klassini yarating. 
class Admin(User):
    """Admin klassi"""
    def __init__(self, ism, familiya, tyil, jins, login):
        super().__init__(ism, familiya, tyil, jins)
        self.login = login
        
        
# 9. Admin klassiga foydalanuvchida yo'q yangi metodlar yozing, masalan, ban_user() metodi konsolga 
# "Foydalanuvchi bloklandi" degan matn chiqarsin.
    def ban_user(self):
        return "Foydalanuvchi bloklandi"
admin = Admin("Kozimjon", "Yoqubov", 1995, "erkak", "kozim95")
print(admin.ban_user())




