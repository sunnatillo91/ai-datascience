# -*- coding: utf-8 -*-
"""
24-DARS LAMBDA  nomsiz funksiya

Created on Wed Jan 17 18:38:52 2024

@author: Sunnatillo
"""

import math

# uzunlik = lambda pi, r: 2*pi*r
# print(uzunlik(math.pi, 10))

# kvadrat = lambda x, y : x**y
# print(kvadrat(2,3))

def daraja(n):
    return lambda x : x**n

kvadrat = daraja(2)
kub = daraja(3)

print(f"3 ning kvadrati {kvadrat(3)} ga, kubi esa {kub(3)} ga teng")