# -*- coding: utf-8 -*-
"""
22-DARS: *args (arguments) va **kwargs (keywords arguments)

Created on Mon Jan 15 20:06:42 2024

@author: Sunnatillo
"""

def summa(*sonlar):  # bu yerda funksiya istalgancha argument qabul qilishi yoki umuman qabul qilmasligi ham mumkin
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi
    return sum(sonlar)

print(summa(1,4))
print(summa(1,3,5,8))

def summa(x,y, *sonlar):  # bu yerda funksiya kamida 2ta ko'pi istalgancha argument qabul qilishi 
    # mumkin sababi f-yada 2 ta majburiy argument kiritildi
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return x+y+sum(sonlar)  # ixchamlashtirilgan ko'rinishi
