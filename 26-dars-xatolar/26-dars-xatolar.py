# -*- coding: utf-8 -*-
"""
26-DARS Ko'p uchraydigan xatolar

Created on Sat Jan 27 14:28:39 2024

@author: Sunnatillo
"""

# AMALIYOT

# Quyida bir nechta kodlar berilgan, kodlar avvalgi darsdagi uy vazifalaridan iborat. Kodlardagi 
# xatolarni toping va to'g'rilang. Har bir dasturda bir nechta xatolar mavjud bo'lishi mumkin. 
# Xatolarni topish uchun dasturlarni bir necha marta, turli qiymatlar bilan bajarib ko'ring. 
# 1)
son = int(input("Juft son kiriting: "))
if son%2 != 0:
    print("Bu son juft emas.")
else:
    print("Rahmat!")
    
# 2)
yosh = int(input("Yoshingiz nechida? "))

if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")

# 3)
x = int(input("Birinchi sonni kiriting: "))
y = int(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")
    
# 4)
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
          print(f"Do'konimizda {mahsulot} bor")
        else:
          print(f"Do'konimizda {mahsulot} yo'q")
else: 
    print("Savatingiz bo'sh")            
   
# 5)
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []
for n in range(5):
    savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing: '))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print("Do'konimizda quyidagi mahsulotlar yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    
# 6)
users = ['alisher1983','aziza','yasina', 'umar']

login = input("Yangi login tanlang:").lower()

if login in users:
    print("Login band, yangi login tanalng!")
else:
    print("Xush kelibsiz!")
