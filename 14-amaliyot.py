# -*- coding: utf-8 -*-
"""
Lug'atlar Amaliyot
Created on Wed Jan  3 16:32:09 2024

@author: sms
"""

# AMALIYOT
# - otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting 
# (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: `Otamning ismi Mavlutdin, 
#  1954-yilda, Samarqand viloyatida tug'ilgan`
otam = {
        'ismi':'yigitali',
        'tyil':1966,
        'viloyat':'samarqand',
        'manzili':'Barkamol'
        }
print(f"Otamning ismi {otam['ismi'].title()}, {otam['tyil']}-yilda {otam['viloyat'].title()} viloyatida tug'ilgan")
# - Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining 
# sevimli taomini konsolga chiqaring: `Alining sevimli taomi osh`
taomlar = {
    'ali':'osh',
    'vali':'dimlama',
    'salim':'jiz',
    'olim':'shashlik',
    'baxrom':'gril'
    }
for ism, taom in taomlar.items():
    # print(taom) 
    print(f"{ism}ning sevimli taomi {taom}")
# - Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if,
# else va hokazo) va har birining qisqacha tarjimasini yozing.

# - Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda
# mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.

# - Yuqoridagi vazifani `if-else` yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.