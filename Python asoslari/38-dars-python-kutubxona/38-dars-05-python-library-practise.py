# -*- coding: utf-8 -*-
"""
38-DARS Python standart kutubxonasi Practise

Created on Tue Feb  6 19:27:45 2024

@author: Sunnatillo
"""
import datetime as dt
from datetime import date
import re


# AMALIYOT
# 1. Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqaring

farq = 0
i = 0
while i<10:
    bugun = dt.date.today()
    keyingi_kun = bugun + dt.timedelta(farq)
    print(f"{i+1}-kun {keyingi_kun}")
    farq += 14
    i += 1

# 2. Ramazon va qurbon hayitigacha qolgan kunlarni konsolga chiqaring
ramazon = dt.date(2024,3,10)
hayit = dt.date(2024,5,19)
farq_hayit = hayit-bugun
farq = ramazon-bugun
print(f"Ramazongacha {farq.days} kun qoldi")
print(f"Hayitgacha {farq_hayit.days} kun qoldi")

# 3. Tug'ilgan kuningizdan bugungi sanagacha qancha yil, oy, kun o'tganini qaytaruvchi 
# funksiya yozing

tyil = dt.date(1995,6,20)
def t_vaqt(tyil):
    """Tug'ilgan kuningizdan bugungi sanagacha qancha yil, oy, kun o'tganini qaytaruvchi 
      funksiya"""
    today = dt.date.today()
    farq_days = (today - tyil).days
    farq_month = int(farq_days/30)
    farq_year = int(farq_month/12)
    print(f"Tug'ilgan kuningizdan hozirga qadar {farq_days} kun, {farq_month} oy \
          {farq_year} yil o'tdi")
          
print(t_vaqt(tyil))

# 4. Foydalanuvchidan telefon raqamini kiritishni so'rang. Kiritlgan qiymatni andoza yordamida 
# tekshiring
andoza = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"

while True:
    phone = input("Telefon raqamingizni kiriting: ")
    if re.match(andoza, phone):
        print("Raqamingiz qabul qilindi")
        break
    else:
        print("Telefon raqam kiritmadingiz ")
# 5. Berilgan matndan veb sahifa manzilini ajratib olyuvchi funksiya yozing. Quyidagi matndan 
# namuna sifatida foydalanishingiz mumkin:
    
matn = """Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi:
https://youtu.be/vsxJPRLXpgI Ushbu darsimizda unittest moduli yordamida 
klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. 
Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"""

def url_sort(matn):
    """Berilgan matndan veb sahifa manzilini ajratib olyuvchi funksiya"""
    andoza = r'https?://\S+'
    url = re.findall(andoza,matn)
    match = []
    if url:
        match.append(url)
        # return match
    else:
        return "Matn ichida veb sahifa manzili topilmadi"
    return match
print(url_sort(matn))