# -*- coding: utf-8 -*-
"""
36-DARS Funksiyalarni tekshirish, UNITTEST moduli

Created on Wed Jan 31 21:14:21 2024

@author: Sunnatillo
"""

import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        name = get_full_name('alijon', 'valiyev')
        self.assertEqual(name, "Alijon Valiyev")
        
    def test_otasining_ismi(self):
        name = get_full_name('alijon', 'valiyev', 'oqilovich')
        self.assertEqual(name, 'Alijon Valiyev Oqilovich')
    
unittest.main()