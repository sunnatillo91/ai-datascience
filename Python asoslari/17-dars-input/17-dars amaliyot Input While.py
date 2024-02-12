# -*- coding: utf-8 -*-
"""
17-dars amaliyot

Created on Mon Jan  8 18:35:48 2024

@author: Sunnatillo
"""

# AMALIYOT

# 1. Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan
#  dasturni to'xtating
# savol = "Yaxshi ko'rgan kitobingizni kiriting"
# savol += "(dasturni to'xtatish uchun 'stop' so'zini yozing)>> "
# kitoblar = ''
# ishora = True
# while ishora:
#     kitoblar = input(savol)
#     if kitoblar == 'stop':
#         ishora = False
#     else:
#         print(kitoblar)
# print("Dastur tugadi ")

# savol = "Yaxshi ko'rgan kitobingizni kiriting"
# savol += "(dasturni to'xtatish uchun 'stop' so'zini yozing)>> "

# while True:
#     kitoblar = input(savol)
#     if kitoblar == 'stop':
#         break
#     else:
#         print(kitoblar)
# print("Dastur tugadi ")
    
# 2. Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000
#  so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi 
#  yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi `exit` yoki `quit` deb yozganda dastur to'xtasin
#  (ikkita shartni ham tekshiring).
# savol = "Yoshingiz nechada?"
# savol += "(Dasturni to'xtatish uchun `exit` yoki `quit` deb yozing) "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
#     if yosh < 7:
#         narx = 2000
#     elif 7 <= yosh <18:
#         narx = 3000
#     elif 18<= yosh < 65:
#         narx = 10000
#     else:
#         narx = 0
#     if narx ==0:
#         print("Sizga chipta tekin")
#     else:
#         print(f"Sizga chipta {narx} so'm")

#     - Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)
# savol = "Yoshingiz nechada?"
# savol += "(Dasturni to'xtatish uchun `exit` yoki `quit` deb yozing) "

# while savol != 'exit' or savol != 'quit':
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
#     if yosh < 7:
#         narx = 2000
#     elif 7 <= yosh <18:
#         narx = 3000
#     elif 18<= yosh < 65:
#         narx = 10000
#     else:
#         narx = 0
#     if narx ==0:
#         print("Sizga chipta tekin")
#     else:
#         print(f"Sizga chipta {narx} so'm")
# print("Dastur tugadi")

# 3. Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib 
# qolmoqda. Xatolarni to'g'rilay olasizmi?
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)    
    if qiymat=='exit':
        break
    son = int(qiymat)
    if son<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{son} ning ildizi {ildiz} ga teng")
        
        