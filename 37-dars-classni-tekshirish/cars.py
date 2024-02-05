# -*- coding: utf-8 -*-
"""
#37-DARS. KLASSNI  TEKSHIRISH

Created on Mon Feb  5 12:09:34 2024

@author: Sunnatillo
"""

class Avto:
    def __init__(self, model, rang, korobka, yil, narh=None, kilometr = 3):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.yil = yil
        self.__kilometr = kilometr
        
    def set_price(self, narh):
        self.narh = narh
            
    def update_km(self, km):
        """Mashinaning km ga yana km qo'shish"""
        if km>0:
            self.__kilometr += km
        else:
            raise ValueError("km manfiy bo'lishi mumkin emas")
    
    def get_info(self):
        info = f"{self.korobka} korobka {self.rang} {self.model} "
        info += f"Ishlab chiqarilgan yili {self.yil}, {self.__kilometr} km yurgan"
        if self.narh:
            info += f" Narxi: {self.narh}"
        return info
    
    def get_km(self):
        return self.__kilometr