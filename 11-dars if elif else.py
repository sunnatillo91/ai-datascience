# -*- coding: utf-8 -*-
"""
# 11-DARS. BIR NECHTA SHARTLARNI TEKSHIRISH
`if-elif-else` zanjiri, `and`, `or` operatorlari bilan tanishamiz

Created on Mon Dec 25 18:30:42 2023

@author: Sunnatillo
"""

# yosh = int(input("Yoshingiz nechada:>>> "))
# if yosh<=4:
#     narx = 0
# elif yosh<=12:
#     narx = 5000
# elif yosh <=18:
#     narx = 8000
# else:
#     narx = 10000
    
# print(f"Sizga kirish {narx} so'm")

# kun = input('Bugun qaysi kun?>>> ')
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print('Bugun dam olish kuni')
# else:
#     print('Bugun ish kuni')
    
# kun = input('Bugun qaysi kun?>>> ')
# harorat = float(input("Havo harorati qanday? "))
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba' and harorat>=30:
#     print('Cho\'milgani ketdik')
# elif kun.lower() == 'shanba' or kun.lower() == 'yakshanba' and harorat<30:
#     print("Bugun tennis o'ynaymiz")
# else:
#     print('Bugun uyda dam olamiz')
    
# narx = 15000  # mijoz taom sotib oldi
# choy = False  # mijoz choy olmadi
# salat = True  # mijoz salat oldi

# # if shart bajarilsa elif va else ni tekshirmaydi
# if choy and salat:  # agar mijoz choy ham salat ham olgan bo'lsa
#     narx = narx+10000  #narxga 10000 so'm qo'shamiz
# elif choy or salat:     # agar choy yoki salat olgan bo'lsa
#     narx = narx+5000    #narxga 5000 so'm qo'shamiz
    
# print(f"Jami {narx} so'm")  #yakuniy narx

# narx = 15000  # mijoz taom sotib oldi
# choy = False  # mijoz choy olmadi
# salat = True  # mijoz salat oldi
# non = 1
# kompot = 1
# assorti = 0

# if choy:  # agar mijoz choy ham salat ham olgan bo'lsa
#     narx = narx+3000  #narxga 3000 so'm qo'shamiz
# if salat:     # agar choy yoki salat olgan bo'lsa
#     narx = narx+5000    #narxga 5000 so'm qo'shamiz
# if non:
#     narx = narx+4000
# if kompot:
#     narx = narx+6000
# if assorti:
#     narx = narx+20000
# print(f"Jami {narx} so'm")  #yakuniy narx

# menu = ['osh', 'qozonkabob', 'shashlik', 'dimlama', 'somsa']
# 'manti' in menu   # menuda manti bormi? natija False
# ovqat = input("Nima ovqat buyurasiz?>>> ")
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi')
# else:
#     print('Uzr bizda bu ovqat yo\'q')        

# menu = ['osh', 'qozonkabob', 'shashlik', 'dimlama', 'somsa']
# ovqat = input("Nima ovqat buyurasiz?>>> ")
# if ovqat.lower() not in menu:
#     print('Uzr bizda bu ovqat yo\'q')
# else: 
#     print('Buyurtma qabul qilindi')       

# menu = ['osh', 'qozonkabob', 'shashlik', 'dimlama', 'somsa']
# # buyurtmalar = ['osh', 'somsa', 'manti', 'dimlama']
# buyurtmalar = []

# if buyurtmalar:   # agar buyurtmalar ro'yxatida biror element bo'lsa ifoda True qaytaradi
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f'Menuda {taom} bor')
#         else:
#             print(f'Uzr, menuda {taom} yo\'q')
# else:
#     print('Savatchangiz bo\'sh')

# AMALIYOT

### Quyidagi dasturlarni alohida fayllarga yozing va bajaring:

# - Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", 
# agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
# son = int(input("Juft son kiriting:>>> "))
# if son%2 ==0:
#     print("Rahmat")
# else:
#     print("Bu son juft emas")

# - Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
#     + Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#     + Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#     + Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
yosh = int(input("Yoshingiz nechada?>>> "))
if yosh < 4 or yosh>60:
    narx = 0
if yosh >= 4 or yosh < 18:
    narx = 10000
if yosh >=18 or yosh <= 60:
    narx = 20000
print(f"Sizga muzeyga kirish uchun chipta narxi {narx} so'm")
# - Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring

# - `mahsulotlar` degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, `savat` degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, `mahsulotlar` ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa `"Mahsulot do'konimizda bor"` aks holda, `"Mahsulot do'konimizda yo'q"` degan xabarlarni chiqaring.

# - Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.

# - `foydalanuvchilar` degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni `foydalanuvchilar` degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, `"Login band, yangi login tanlang!"` aks holda `"Xush kelibsiz, foydalanuvchi!"` xabarini chiqaring.

# - Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.
        