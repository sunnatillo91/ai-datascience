# -*- coding: utf-8 -*-
"""
08-dars  LISTS
Created on Wed Dec 20 21:11:36 2023

@author: Sunnatillo
"""

#Sort ro'yxatni alifbo tartibi bo'yicha tartiblash
cars = ['Bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort()  #ro'yxatni alifbo tartibi bo'yicha tartiblash
# > **Diqqat!** Tartiblashda katta harflar kichik harflardan avval kelishini hisobga oling. Agar matndagi so'zlarning bosh 
# harfi katta-kichik aralash yozilgan bo'lsa, ularni bir ko'rinishga keltirib olish maqsadga muvofiq bo'ladi.
# cars.sort(reverse=True)   #ro'yxatni alifboga teskari tartib bo'yicha tartiblash
# print(cars)

# print(sorted(cars))  # asl ro'yxatni o'zgartirmagan holda ro'yxatdagi elementlarni tartiblab chiqarish

# mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
# print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)

# # sorted() funktsiyasi yordamida teskari tartiblash uchun ham reverse=True argumentini beramiz:

# print(sorted(mehmonlar, reverse=True))

# # Ro'yxatni teskari tarafdan chiqarish uchun reverse f-ya ishlatiladi
# mehmonlar.reverse()
# print(mehmonlar)

# # Ro'yxat uzunligini aniqlash uchun len() metodi bor ekan

# uzunlik = len(mehmonlar)

# sonlar = list(range(0,10))

# juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
# toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
# print("Juft sonlar: ", juft_sonlar)
# print("Toq sonlar: ", toq_sonlar)

# SONLI RO'YXAT USTIDA SODDA AMALLAR
# Pythonda ro'yxatlar ustida ba'zi sodda amallarni ham bajarish mumkin. Misol uchun ro'yxatdagi eng kichik sonni topish uchun min() funktsiyasidan, eng katta sonni topish uchun esa max() funktsiyasidan, sonlarning yig'indisini topish uchun esa sum() funktsyasidan foydalansak bo'ladi:

# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)

# RO'YXATNI KESISH
# cars = ['Bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[0:3] # 0-indeskdan boshlab 3 ta element ajratib olamiz
# print(my_cars) 
# ['bmw', 'mercedes benz', 'volvo']
# # Diqqat! Python 2-indeksdan bitta avval to'xtaydi. Yuqoridagi misolda ham 0,1,2-elementlar ajratib olindi.

# # Bu usul bilan ro'yxatning istalgan joyidan bo'lishimiz mumkin:

# print(cars[2:5]) # 2-3-4-elementlarni ajratib olamiz (5 kirmaydi)
# ['volvo', 'general motors', 'tesla']
# # Agar boshlang'ich indeksni bermasangiz, Python avtomat ravishda 0 indeksdan boshlab kesadi. Agar 2-indeksni kiritmasangiz, 
# # ro'yxat oxirigacha kesadi:

# print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
# print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi
# # Ro'yxat orasidan dastlabki 3 ta mashinani chiqarish
# print(cars[0:3])

#RO'YXATDAN NUSXA OLISH

# sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# sonlar2 = sonlar[:] # [:] ro'yxatni to'liq ko'chirib oladi
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

# TUPLES - O'ZGARMAS RO'YXAT

# tomonlar = (20, 30, 55.2)
# print(tomonlar)

# # Tuple ichidagi elementlarga huddi ro'yxat elementlariga murojat qilingani kabi murojat qilinaveradi:

# toys = ('bus','car','bear','dino','snake','lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])

# toys.append('rabbit')  # toys.append('rabbit') # AttributeError: 'tuple' object has no attribute 'append'

# Agar Tuple ga o'zgartirish talab qilinsa, yagona yo'li o'zgarmas ro'yxatni list() funktsiyasi yordamida List (oddiy ro'yxat) 
# ko'rinishiga keltirib olish, o'zgarishlarni bajarsih va qaytarib tuple() funktsiyasi yordamida o'zgarmas ro'yxatga o'tkazish mumkin:

toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# Ro'yxatga o'zgartirishlar kiritamiz
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
print(toys)
