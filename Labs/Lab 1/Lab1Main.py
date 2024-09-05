#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:33:21 2024

@author: jacksonbraun
"""
#background code im caught up on
x = [1, 2, 3];

x2 = x*3;

import numpy as np



import matplotlib.pyplot as plt




#section 3

x = np.linspace(0,1,10)
y = np.arange(10)
x1 = x[0]
x2 = x[1]
x3 = x[2]
print('the first three intries of x are ', x1, x2, x3)


#3.4-3.6
w = 10**(-np.linspace(1,10,10))
x = np.arange(np.size(w))


plt.plot(x,w)

plt.xlabel("x")
plt.ylabel("w")

s = w*3

plt.plot(x,s)

plt.show()