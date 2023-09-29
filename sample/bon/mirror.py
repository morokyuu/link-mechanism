# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 21:41:41 2023

@author: square
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def mirrorY():
    return np.array([
        [         -1,          0,   0],
        [          0,          1,   0],
        [          0,          0, 1.0]
        ])

def tr(x,y):
    return np.array([
        [        1.0,          0,   x],
        [          0,        1.0,   y],
        [          0,          0, 1.0]
        ])

def scale(r):
    return np.array([
        [          r,          0,   0],
        [          0,          r,   0],
        [          0,          0, 1.0]
        ])

df = pd.read_csv("shadow.txt",sep='\t')

xy1 = np.vstack((df['x'],df['y'],np.ones(df.shape[0])))
xy2 = np.vstack((df['x'],df['y'],np.ones(df.shape[0])))

xy2 = np.fliplr(xy2)

xy1 = tr(-170,0) @ xy1
xy2 = tr(-170,0) @ xy2

xy = np.hstack((xy1, (mirrorY() @ xy2))) ## [::-1]=reverse

xy = scale(0.21) @ xy

plt.plot(xy[0],xy[1])


print("x,y")
for x,y in zip(xy[0],xy[1]):
    print(f'{x:.3f},{y:.3f}')
