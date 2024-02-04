# -*- coding: utf-8 -*-
"""
36-dars unittest practise

Created on Sun Feb  4 17:09:49 2024

@author: Sunnatillo
"""

from practise import juft_son
import unittest
class JuftSonTest(unittest.TestCase):
    def test_juft_son(self):
        self.assertTrue(juft_son([1,2,3,5]))
        self.assertTrue(juft_son([5,2,8,10]))
        
unittest.main()