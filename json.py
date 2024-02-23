# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:34:20 2023

@author: yekta
"""
import json

with open ('data.json','r') as file:
    data = json.load(file)
    
sin_data = data ['sin']
print(sin_data)

cos_data = data ['cos']
print(cos_data) 