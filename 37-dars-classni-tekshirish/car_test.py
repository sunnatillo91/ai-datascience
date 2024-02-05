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
        model = "Malibu"
        rang = "Qora"
        korobka = "Avtomat"
        yil = 2023
        self.narh = 40000
        self.kilometr = 15000
        self.avto1 = Avto(model, rang, korobka, yil)
        self.avto2 = Avto(model, rang, korobka, yil, narh=self.narh)
        
    def test_create(self):
        # Qiymatlar mavjudligini assertIsNotNone metodi bilan tekshiramiz
        self.assertIsNotNone(self.avto1.model)
        self.assertIsNotNone(self.avto1.rang)
        self.assertIsNotNone(self.avto1.korobka)
        self.assertIsNotNone(self.avto1.yil)
        
        # Qiymat mavjud emasligini assertIsNone metodi bilan tekshiriladi
        self.assertIsNone(self.avto1.narh)
        
        # Qiymat tengligini assertEquals metodi bilan tekshiramiz
        self.assertEquals(3, self.avto1.get_km())
        # self.assertEqual(self.model, self.avto1.model)
        # avto2 narxini tekshiramiz
        self.assertEquals(self.narh, self.avto2.narh)
        
unittest.main()