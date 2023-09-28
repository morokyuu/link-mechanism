# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 22:28:48 2023

@author: square
"""

import numpy as np
import matplotlib.pyplot as plt

th = np.linspace(0, 2*np.pi,50)
x = 2 * np.cos(th)
y = 1.5 * np.sin(th)

fig,ax = plt.subplots()
ax.scatter(x,y)

ax.set_aspect('equal')