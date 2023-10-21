# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 23:11:32 2023

@author: square
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def rotZ(th):
    return np.array([
        [ np.cos(th), np.sin(th), 0.0],
        [-np.sin(th), np.cos(th), 0.0],
        [          0,          0, 1.0]
        ])

def tr(x,y):
    return np.array([
        [        1.0,          0,   x],
        [          0,        1.0,   y],
        [          0,          0, 1.0]
        ])

def scale(ratio):
    return np.array([
        [      ratio,          0, 0.0],
        [          0,      ratio, 0.0],
        [          0,          0, 1.0]
        ])

df = pd.read_csv("../foot.txt",sep=",")
foot = np.vstack((df['x'],df['y'],np.ones(df.shape[0])))
foot = np.hstack((foot, np.vstack((df['x'].head(1),df['y'].head(1),1))))

length = df['y'].max()
foot = tr(0,-length/2) @ foot

sc_foot = scale(16/24.0) @ foot

fig,ax = plt.subplots()
ax.plot(foot[0], foot[1])
ax.plot(sc_foot[0], sc_foot[1])
ax.grid()
ax.set_aspect('equal')

print("x,y")
for x,y in zip(foot[0],foot[1]):
    print(f"{x:.3f},{y:.3f}")
