# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 13:48:32 2021

@author: japem
"""

import preheat_open as ph

loc = 2245
b = ph.Building(loc)
print(b)

start = "2021-09-10 00:00:00"
stop = "2021-09-22 12:00:00"
res = "raw"

room_1 = b.query_units(name='room_1')[0]
room_1.load_data(start,stop,res)

print(room_1.data)




