# -*- coding: utf-8 -*-
"""
36-dars unittest practise

Created on Sun Feb  4 17:39:40 2024

@author: Sunnatillo
"""
import unittest
from practise import fibonacci

class FibonacciTest(unittest.TestCase):
    def test_fibonacci(self):
        self.assertTrue(fibonacci(13))
        # self.assertIn(fibonacci(6), 8)
        
unittest.main()