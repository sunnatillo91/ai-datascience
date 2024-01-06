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

print("Kiritilgan sonning kvadratini qaytaruvchi dastur")
savol = "Istalgan son kiriting:>> "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing:) "
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(int(qiymat)**2)
print("Dastur tugadi")
