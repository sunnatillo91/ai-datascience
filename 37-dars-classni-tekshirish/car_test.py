# -*- coding: utf-8 -*-
"""
#37-DARS. KLASSNI  TEKSHIRISH

Created on Mon Feb  5 12:40:55 2024

@author: Sunnatillo
"""

import unittest
from cars import Avto

class CarTest(unittest.TestCase):
    """Car klassini tekshirish uchun test"""
    def setUp(self):
        self.model = "Malibu"
        self.rang = "Qora"
        self.korobka = "Avtomat"
        yil = 2023
        self.narh = 40000
        self.__kilometr = 15000   
        self.avto1 = Avto(self.model, self.rang, self.korobka, yil)
        self.avto2 = Avto(self.model, self.rang, self.korobka, yil, narh=self.narh)
        
    def test_create(self):
        # Qiymatlar mavjudligini assertIsNotNone metodi bilan tekshiramiz
        self.assertIsNotNone(self.avto1.model)
        self.assertIsNotNone(self.avto1.rang)
        self.assertIsNotNone(self.avto1.korobka)
        self.assertIsNotNone(self.avto1.yil)
        
        # Qiymat mavjud emasligini assertIsNone metodi bilan tekshiriladi
        self.assertIsNone(self.avto1.narh)
        
        # Qiymat tengligini assertEquals metodi bilan tekshiramiz
        self.assertEquals(0, self.avto1.get_km())
        self.assertEqual(self.model, self.avto1.model)
        # avto2 narxini tekshiramiz
        self.assertEquals(self.narh, self.avto2.narh)
        
    def test_set_price(self):
        new_price = 45000
        self.avto2.set_price(new_price)
        self.assertEqual(new_price, self.avto2.narh)
        
    def test_add_km(self):
        # 1 musbat qiymat berib tekshirib ko'riladi
        self.avto1.update_km(self.__kilometr)
        self.assertEqual(self.__kilometr, self.avto1.get_km())
        self.avto1.update_km(3000)
        self.assertEqual(18000, self.avto1.get_km())
        # 2 manfiy qiymat berib ko'ramiz
        new_km = -5000
        try:
            self.avto1.update_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)
            
    def test_get_info(self):
        avto_info = "Avtomat korobka Qora Malibu Ishlab chiqarilgan yili 2023, 0 km yurgan"
        self.assertEqual(avto_info, self.avto1.get_info())
        # avto1 narxi va km ni o'zgartiramiz
        self.avto1.update_km(6000)
        self.avto1.set_price(35000)
        avto_info = "Avtomat korobka Qora Malibu Ishlab chiqarilgan yili 2023, 6000 km yurgan Narxi: 35000"
        self.assertEqual(avto_info, self.avto1.get_info())
        # self.assertEqual(self.korobka, self.avto1.korobka)
        
    def test_get_km(self):
        self.avto1.update_km(3000)
        self.assertEqual(3000, self.avto1.get_km())
unittest.main()