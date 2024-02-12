# -*- coding: utf-8 -*-
"""
19-dars FUNCTIONS (FUNKSIYALAR)
Created on Tue Jan  9 20:50:27 2024

@author: Sunnatillo
"""

def toliq_ism(ism, familiya):
    """Foydalanuvchi ismi va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")
toliq_ism('olim', "hakimov")
#parametrlarni kiritishda funksiyada ko'rsatilgan tartibda kiritish zarur aks xolda xatolik kelib chiqadi
# toliq_ism('hakimov', 'olim')  
# yuqoridagi xato oldini olish uchun parametrlar bilan kiritish ham mumkin
toliq_ism(familiya='hakimov', ism='olim')


def yosh_hisobla(ism, tyil):
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{ism.title()} {2024-tyil} yoshda")
    
yosh_hisobla('sunnatillo', 1991)