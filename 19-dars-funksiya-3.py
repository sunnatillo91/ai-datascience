# -*- coding: utf-8 -*-
"""
19-dars FUNCTIONS (FUNKSIYALAR)
Created on Tue Jan  9 20:50:27 2024

@author: Sunnatillo
"""

# def yosh_hisobla(tyil, joriy_yil=2024):
#     """Foydalanuvchi tug'ilgan yilga ko'ra uning yoshini hisoblaydigan dastur"""
#     print(f"Siz {joriy_yil-tyil} yoshdasiz")

# #Yuqoridagi funksiyada joriy yilga standart(default) qiymat berilgan    
# yosh_hisobla(1991)
# yosh_hisobla(1991,2024)


# # AMALIYOT
# # 1. Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
# def yosh_hisobla(ism, yosh):
#     """Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya"""
#     print(f"{ism.title()} siz {2023-yosh}-yilda tug'ilgan ekansiz")
# yosh_hisobla("olim", 27)
# 2. Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
# def kvadrat_kub(son):
#     """Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya"""
#     print(f"{son} ning kvadrati {son**2} ga teng \n"
#           f"{son} ning kubi {son**3} ga teng")
    
# kvadrat_kub(8)
# 3. Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
# def juft_toq(son):
#     """Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya"""
#     if son%2 == 0:
#         print(f"{son} juft son")
#     else:
#         print(f"{son} toq son")
# juft_toq(12)
# juft_toq(13)
# 4. Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar 
# sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
# def katta_kichik(son1, son2):
#     """Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya"""
#     if son1>son2:
#         print(f"Katta son {son1}")
#     elif son1<son2:
#         print(f"Katta son {son2}")
#     else:
#         print("Sonlar teng")
# katta_kichik(15, 56)
# katta_kichik(26, 15)
# katta_kichik(12, 12)
# 5. Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya yozing.
# def daraja(x, y):
#     """Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya"""
#     print(f"{x}^{y}={x**y}")
    
# daraja(5, 3)
# 6. Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
# def daraja(x, y=2):
#     """Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya"""
#     print(f"{x}^{y}={x**y}")
    
# daraja(5)
# 7. Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini 
# tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
def qoldiqsiz_bulinish(son):
    """Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini 
    tekshiruvchi funksiya"""
    for n in range(2,11):
        if son%n == 0:
            print(f"{son}/{n} = {son/n}")
        else:
            continue
        n += 1
qoldiqsiz_bulinish(25)
qoldiqsiz_bulinish(30)


