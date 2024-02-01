# -*- coding: utf-8 -*-
"""
36-dars Unittest

Created on Thu Feb  1 21:35:06 2024

@author: Sunnatillo
"""
from circle import getArea, getPerimeter
import unittest

class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(5),78.53975)
        self.assertAlmostEqual(getArea(12), 452.38896)
        
    def test_perimeter(self):
        self.assertAlmostEqual(getPerimeter(10), 62.8318)
        self.assertAlmostEqual(getPerimeter(4), 25.13272)

unittest.main()

