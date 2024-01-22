# -*- coding: utf-8 -*-
"""
25-DARS Data Science va Sun'iy Intellekt Praktikum

KLASS VA OBYEKT

Created on Sun Jan 21 17:29:46 2024

@author: Sunnatillo
"""

matn = "Assalomu alaykum "

class Kompyuter:
    def __init__(self, model, ram, hdd, gpu, cpu):
        self.model = model
        self.ram = ram
        self.hdd = hdd
        self.gpu = gpu
        self.cpu = cpu
        
    def info(self):
        inf = f"{self.model} RAM: {self.ram}, HDD: {self.hdd}, GPU: {self.gpu}, CPU: {self.cpu}"
        return inf
    
mackbook = Kompyuter("Apple mackbook", "8GB", "512GB", "M1", "M1")
    