# -*- coding: utf-8 -*-
"""
28-DARS JSON

Created on Tue Jan 30 16:13:24 2024

@author: Sunnatillo
"""

import json
# import googlemaps
# from apikey import APIKEY

# # GoogleMaps
# gmaps = googlemaps.Client(key=APIKEY)

# data = gmaps.geocode('Olmazor, Tashkent, Uzbekistan')

# g = json.dumps(data[0], indent=4, sort_keys=True)
# print(g)

x = 10
x_json = json.dumps(x) # bu holatda x str ga o'tkaziladi

y = 5.5
y_json = json.dumps(y)

m = True
m_json = json.dumps(m)