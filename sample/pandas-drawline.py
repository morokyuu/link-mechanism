# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:56:25 2023

@author: square
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def drawLine(ax,x0,y0,x1,y1,color='blue'):
    ax.plot(np.array([x0,x1]),np.array([y0,y1]),color=color)


r = 10

df = pd.DataFrame()

df['th'] = np.linspace(0,2*np.pi,9)
df['x'] = r * np.cos(df['th'])
df['y'] = r * np.sin(df['th'])

fig,ax = plt.subplots()
ax.scatter(df["x"],df["y"])
ax.set_aspect('equal')

for i in range(df.shape[0]-1):
    drawLine(ax,df['x'][i],df['y'][i],df['x'][i+1],df['y'][i+1],'brown')
    print(i)


# こうやったらqueryと似たようなことができる
# df[(df["th"] > 2) & (df["th"] < 4)]

