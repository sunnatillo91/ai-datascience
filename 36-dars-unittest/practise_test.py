# -*- coding: utf-8 -*-
"""
36-dars Unittest practise 

Created on Fri Feb  2 19:16:41 2024

@author: Sunnatillo
"""
from practise import eng_katta
import unittest

class KattaSonTest(unittest.TestCase):
    def test_kattason(self):
        self.assertEqual(eng_katta(8,7,9), 9)
        self.assertEqual(eng_katta(8,12,5), 12)
        
unittest.main()
