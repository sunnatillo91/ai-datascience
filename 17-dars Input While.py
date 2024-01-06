# -*- coding: utf-8 -*-
"""
17-dars INPUT() VA WHILE

Created on Sat Jan  6 16:29:07 2024

@author: Sunnatillo Xayrullayev
"""

# input()

# ism = input("Ismingiz nima?>> ")
# savol = f"Salom {ism.title()} yoshingiz nechada?>> "
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Bo'yingiz necha metr?>> ")
# height = float(height)

# while()

son = 1  # songa 1 qiymat beramiz
# while son<=5:       #toki son 5 dan kichik yoki teng ekan ...
#     print(son, end=' ')  # sonni konsolga chiqaramiz
#     son = son+1  # son+=1   songa 1 ni qo'shamiz
# print("Dastur tugadi")
    
# input() and while()

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur")
# savol = "Istalgan son kiriting:>> "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing:) "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(int(qiymat)**2)
# print("Dastur tugadi")

# Ishora

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur")
# savol = "Istalgan son kiriting:>> "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing:) "
# ishora = True

# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(int(qiymat)**2)
# print("Dastur tugadi")

# # break while
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur")
# savol = "Istalgan son kiriting:>> "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing:) "

# while True:     #abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break   #tsiklni to'xtatish
#     else:
#         print(int(qiymat)**2)
# print("Dastur tugadi")

# break for 
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 6:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")
    
# continue
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 6:   # agar son 6 ga teng bo'lsa
#         continue  #siklni boshiga qaytadi, ya'ni 6 ni tashlab keyingi songa o'tib ketadi
#     print(f"{son} ning kvadrati {son**2} ga teng")
    
# continue while
# son = 0
# while son <10:
#     son += 1
#     if son%2 !=0:
#         continue
#     else:
#         print(son)

# infinite loop abadiy sikl
# son = 0
# while son <10:
#     # son += 1  ushbu qator yozilmasa abadiy siklga tushib qoladi (to'xtatish uchun konsolda Ctrl+C)
#     if son%2 !=0:
#         continue
#     else:
#         print(son)

# son = 0
# while son <10:
#     if son%2 !=0:
#         continue
#     else:
#         print(son)
#     son += 1  # bu qator noto'g'ri joyga yozilgani sabab abadiy siklga tushib qoladi
    
# son = 1
# while son > 0:
#     son += 1
#     if son%2 !=0:
#         continue
#     else:
#         print(son)

# AMALIYOT

# 1. Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi 
# bilan dasturni to'xtating
# savol = "Yaxshi ko'rgan kitoblaringiz nomini kiriting: "
# savol += "(To'xtatish uchun 'stop' so'zini yozing) "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'stop':
#         break
#     else:
#         print(qiymat.title())
        
# savol = "Yaxshi ko'rgan kitoblaringiz nomini kiriting: "
# savol += "(To'xtatish uchun 'stop' so'zini yozing) "
# while True:
#     qiymat = input(savol)
#     if qiymat == 'stop':
#         break
#     else:
#         print(qiymat.title())
        
# savol = "Yaxshi ko'rgan kitoblaringiz nomini kiriting: "
# savol += "(To'xtatish uchun 'stop' so'zini yozing) "
# qiymat = ''
# while qiymat != 'stop':
#     qiymat = input(savol)
#     if qiymat != 'stop':
#         print(qiymat.title())
        
# 2. Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 
# so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi 
# yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi `exit` yoki `quit` deb yozganda dastur 
# to'xtasin (ikkita shartni ham tekshiring).
# savol = "yoshingizni kiriting:"
# savol += "(dasturni to'xtatish uchun 'exit' yoki 'quit' deb yozing) "
# qiymat = ''
# while qiymat != 'exit' or qiymat != 'quit':
#     qiymat = input(savol)
#     if qiymat != 'exit' or qiymat != 'quit':
#         if int(qiymat) < 7:
#             narx = 2000
#         elif int(qiymat) >= 7 and int(qiymat) < 18:
#             narx = 3000
#         elif int(qiymat) >= 18 and int(qiymat) < 65:
#             narx = 10000
#         elif int(qiymat) >= 65:
#             narx = 0
#         print(f"Sizga chipta narxi {narx} so'm")
    
#     - Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)

# savol = "yoshingizni kiriting:"
# savol += "(dasturni to'xtatish uchun 'exit' yoki 'quit' deb yozing) "
# while True:
#     qiymat = input(savol)
#     if qiymat != 'exit' or qiymat != 'quit':
#         yosh = int(qiymat)
#         if yosh < 7:
#             narx = 2000
#         elif 7 <= yosh < 18:
#             narx = 3000
#         elif 18 <= yosh < 65:
#             narx = 10000
#         elif yosh >= 65:
#             narx = 0
#         print(f"Sizga chipta narxi {narx} so'm")
#     else:
#         break
    
# savol = "yoshingizni kiriting:"
# savol += "(dasturni to'xtatish uchun 'exit' yoki 'quit' deb yozing) "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     else:
#         yosh = int(qiymat)
#         if yosh < 7:
#             narx = 2000
#         elif 7 <= yosh < 18:
#             narx = 3000
#         elif 18 <= yosh < 65:
#             narx = 10000
#         else:
#             narx = 0
#         if narx == 0:
#             print("Sizga chipta tekin")
#         else:
#             print(f"Sizga chipta narxi {narx} so'm")
# 3. Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy holatlarda tsikl abadiy 
# qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
        
        
        