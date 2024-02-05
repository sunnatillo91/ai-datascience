# -*- coding: utf-8 -*-
"""
#36-DARS. FUNKSIYALARNI TEKSHIRISH

Created on Thu Feb  1 22:00:56 2024

@author: Sunnatillo
"""

import unittest
from tubsonmi import tubSonmi

class tubSonTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(tubSonmi(7))
        self.assertTrue(tubSonmi(193))
        self.assertTrue(tubSonmi(547))
    def test_false(self):
        self.assertFalse(tubSonmi(6))
        self.assertFalse(tubSonmi(265))
        self.assertFalse(tubSonmi(489))
        
unittest.main()