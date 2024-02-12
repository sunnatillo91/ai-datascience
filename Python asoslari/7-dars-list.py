# -*- coding: utf-8 -*-
"""
07-dars  LIST
Created on Mon Dec 18 21:08:13 2023

@author: Sunnatillo
"""

# bozorlik = ['un', "yog'", "go'sht", 'tuxum']
# print(bozorlik)
# mahsulot = bozorlik.pop(2)  # ro'yxatdan go'shtni sug'urib olamiz
# print("Men " + mahsulot + " sotib oldim")
# print("Olinmagan maxsulotlar ", bozorlik)


# mevalar = ['olma', 'anor', 'olcha', 'uzum']  #mevalar ro'yxati
# narxlar = [200, 1555, 61000, 5665, -45, 36.6]   #narxlar ro'yxati
# sonlar = ['bir', 'ikki', 'uch', 4, 5]   #sonlar va aralash matnlar
# narhlar = [12000, 18000, 10900, 22000]
# narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
# narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
# narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
# print(narhlar)

# ismlar = []  #bo'sh ro'yxat

# print(mevalar[-1])  #natija uzum
# print(mevalar[0])   #natija olma
# print(mevalar[0].title())   #natija Olma

# mevalar[0] = 'nok'
# print(mevalar[0])   #natija nok

# mevalar.append('shaftoli')      #mevalar ro'yxati oxiriga shaftoli qo'shildi
# mevalar.insert(2, 'banan')   #mevalar ro'yxatida uchinchi o'ringa banan qo'shildi

# cars = []
# cars.append('Lacetti')
# cars.append('Nexia')
# cars.append('Spark')   # ro'yxat oxiridan boshlab element qo'shish

# cars.insert(1, 'Cobalt')  #indexni ko'rsatgan holda element qo'shish
# del cars[1]   # indeksi 2 bo'lgan elementni ro'yxatdan o'chirish
# cars.remove("Nexia")  # ro'yxatdagi birinchi Nexiani o'chiradi

# print(cars)

# Amaliyot
# Quyidagi mashqlarni bajaring:

# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:

# ismlar = ["Abdulloh", "Muhammad", "Ahmad"]
# print("Salom " + ismlar[1] + ", bugun choyxonaga boramizmi? ")
# print(ismlar[2] + ',', " choyxonaga boramizmi? ")

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
# sonlar = [200, 1555, 61000, 5665, -45, 36.6]

# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
# sonlar.append(365)
# sonlar.insert(1, 160)
# sonlar[2] = sonlar[2]+45
# print(sonlar[2])
# sonlar[6] = 42.2
# print(sonlar)

# t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
# t_shaxslar = ["Muhammad alayhissalom", "Amir Temur", "Imom Buxoriy"]
# z_shaxslar = ['Shayx Muhammad Sodiq Muhammad Yusuf', "Ilon Mask", '...']

# # Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
# print("Men tarixiy shaxslardan " + t_shaxslar.pop(0) + ' bilan, \nzamonaviy shaxslardan esa ' + 
#       z_shaxslar.pop(0) + " bilan suhbat qilishni istardim" )

# friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friends = []
friends.append("Shuhrat")
friends.append("Oybek")
friends.append("Olmos")
friends.append("Nurjahon")
friends.append("Baxrom")

# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
friends.remove("Olmos")
friends.remove("Baxrom")

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.insert(0, "Shaxboz")
friends.insert(2, "Feruz aka")
friends.insert(5, "Mehriddin")
# Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga 
#kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(2))