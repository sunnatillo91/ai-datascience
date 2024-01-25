# -*- coding: utf-8 -*-
"""
25-DARS OOP Incapsulation

Created on Thu Jan 25 21:00:43 2024

@author: Sunnatillo
"""

from avto import Avto
            
avto1 = Avto("GM", "Malibu", "Qora", 2023, 30000, 100)
avto2 = Avto("GM", "Lacetti", "Oq", 2023, 20000, 200)
avto3 = Avto("GM", "Cobalt", "Qora", 2023, 15000, 150)
print(avto1.get_km())
print(avto1.get_num_avto())