# -*- coding: utf-8 -*-
"""
23-dars: MODULLAR

Created on Tue Jan 16 19:05:47 2024

@author: Sunnatillo
"""

# Boshqa modul(fayllar)dan funksiyalarni import qilib foydalanishni turli usullari bor:
    # 1-usul
# import avto_info_mod
# avto1 = avto_info_mod.avto_info('GM', 'Malibu', "Qora", 'avtomat', 2022, 35000)
# avto_info_mod.info_print(avto1)

    # 2-usul modul nomini qisqartirish
import avto_info_mod as aim   
avto1 = aim.avto_info('GM', 'Malibu', "Qora", 'avtomat', 2022, 35000)
aim.info_print(avto1)

    # 3-usul moduldan zarur funksiyalarni chaqirish
from avto_info_mod import avto_info, info_print
avto1 = avto_info('GM', 'Lacetti', "Qora", 'avtomat', 2022, 25000)
info_print(avto1)

    # 4-usul moduldan zarur funksiyalarni nomini o'zgartirib chaqirish (f-ya nomi uzun bo'lganda
    # yoki bir xil nomli f-ya bo'lganda qo'llash qulay)
from avto_info_mod import avto_info as ainfo, info_print as iprint
avto1 = ainfo('GM', 'Gentra', "Qora", 'avtomat', 2022, 20000)
iprint(avto1)

    # 5-usul moduldan barcha f-yani chaqirish 
    # (modulda ko'plab f-ya va o'zgaruvchilar bo'lsa bu usuldan foydalanmaslik tavsiya qilinadi)
from avto_info_mod import *
avto1 = avto_info('GM', 'Lacetti', "Qora", 'avtomat', 2022, 25000)
info_print(avto1)

# PYTHON MODULLARI
# Python dasturlash tili tayyor modullar bilan keladi, modullarning to'liq ro'yxatini quyidagi 
# bo'glama orqali kirib ko'rishingiz mumkin: https://docs.python.org/3/py-modindex.html