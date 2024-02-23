# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:48:02 2023

@author: yekta
"""


import math                                               # call the math fonction
import matplotlib.pyplot as plt                           # call the library this means short type for this long name
import numpy as np                                        # call the numpy
import json                                               # call the json fonction


# Call the json file 
with open ('data.json','r') as file:                      # call the json file which name is data.json and short name is file
    data = json.load(file)
    
    
    
sin_dt = data ['sin']                                     # sin data from the file
print(sin_dt)



cos_dt = data ['cos']                                     # cos data from the file
print(cos_dt) 
    

# Graph 
x = np.linspace(-math.pi,math.pi,100)                     # graph's limits

sin_sum = 0
cos_sum = 0

    
for sinfr in sin_dt:                                     # use the json for sin and show freq on the graph

    siny = np.sin(sinfr['freq']*x)*sinfr['a']
    sin_sum += siny
  
    
plt.plot(x, sin_sum,                                     # print sin graph 
         linewidth=5,
         color='yellow')


    
for cosfr in cos_dt:                                      # use the json for cos and show freq on the graph

    cosy = np.cos(cosfr['freq']*x)*cosfr['a'] 
    cos_sum += cosy
    
    
plt.plot(x, sin_sum+cos_sum,                             # print graphs together 
         linewidth=5,
         color='blue')

    