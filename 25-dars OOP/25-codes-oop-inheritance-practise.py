# -*- coding: utf-8 -*-
"""
25-DARS OOP Inheritance and Polymorphism PRACTISE

Created on Thu Jan 25 16:52:06 2024

@author: sms
"""

# AMALIYOT
# 1. Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. Bu xususiyat parametr sifatida 
# uzatilmasin va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])
class Talaba:
    """Talaba klasi"""
    def __init__(self, ism, familiya, bosqich, manzil):
        self.ism = ism
        self.familiya = familiya
        self.bosqich = bosqich
        self.manzil = manzil
        self.fanlar = []
        
    def get_info(self):
        info = f"{self.ism} {self.familiya} "
        info += f"{self.bosqich} - bosqich talabasi "
        return info
    
# 2. Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.


# 3. Talaba klassiga fanga_yozil() degan yangi metod yozing. Bu metod parametr sifatida Fan 
# klassiga tegishli obyektlarni qabul qilib olsin va talabaning fanlar ro'yxatiga qo'shib qo'ysin.
# 4. Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun remove_fan() metodini yozing. 

# 5. Agar bu metodga ro'yxatda yo'q fan uzatilsa "Siz bu fanga yozilmagansiz" xabarini qaytarsin.

# 6. Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor, 
# Foydalanuvchi, Sotuvchi, Mijoz va hokazo)

# 7. Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.

# 8. Barcha yangi klasslar uchun get_info() metodini qayta yozib chiqing.

# 9. Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun Foydalanuvchi 
# klassidan Admin klassini yarating. 

# 10. Admin klassiga foydalanuvchida yo'q yangi metodlar yozing, masalan, ban_user() metodi 
# konsolga "Foydalanuvchi bloklandi" degan matn chiqarsin.