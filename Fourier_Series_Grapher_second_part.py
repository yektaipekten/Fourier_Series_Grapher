# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 15:10:35 2023

@author: yekta
"""

import math                                              # call the math fonction
import matplotlib.pyplot as plt                          # call the library this means short type for this long name
import numpy as np                                       # call the numpy with short name


x = np.linspace(-math.pi,math.pi,360)                    # graph limits

y = np.sin(x)

#z = list(zip(x,y))

#zz = sorted(z, key = lambda z: z[1], reverse=True)

sum = 0
r = np.sin(1)
for i in range(1,200,2):                                # square wave's limits
   # print(i)
    sum = sum + (np.sin(i*y)/i)
    
print(sum)
plt.plot(x,sum,linewidth = 2, color = 'blue')