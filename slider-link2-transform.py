# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:03:11 2023

@author: square
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

def drawLine(ax,x0,y0,x1,y1):
    ax.plot(np.array([x0,x1]),np.array([y0,y1]))

def drawPolyline(ax,poly):
    poly = poly.T
    poly = np.vstack((poly,poly[0,:]))
    for i in range(poly.shape[0]-1):
        drawLine(ax,poly[i,0],poly[i,1],poly[i+1,0],poly[i+1,1])

r = 0.012
L = 0.1
Lx = 0.055
NUM = 20

df = pd.DataFrame()

th = np.linspace(0.001,np.pi*2,NUM)
x = r * np.cos(th)
y = r * np.sin(th)
alpha = np.arctan(y/Lx - x)
l = np.sqrt((Lx - x)**2 + (0 - y)**2)
px = (L - l)*np.cos(-alpha) + Lx
py = (L - l)*np.sin(-alpha)

df['x'] = x
df['y'] = y
df['alpha'] = alpha
df['px'] = px
df['py'] = py

fig,ax = plt.subplots()
ax.scatter(Lx,0)
ax.scatter(df['x'],df['y'])
ax.scatter(df['px'],df['py'])
ax.set_aspect('equal')
ax.grid()


x = 0.04
y = 0.005
a= 0.2


box = np.array([[r,r,-r,-r],[r,-r,-r,r],[1,1,1,1]])

for i in range(df.shape[0]):
    fig,ax = plt.subplots()
    
    a = df['alpha'][i]
    px = df['px'][i]
    py = df['py'][i]
    
    x,y = df['x'][i],df['y'][i]
    px,py = df['px'][i],df['py'][i]
    
    ax.scatter(x,y)
    ax.scatter(px,py)
    drawLine(ax, x,y,px,py)
    
    boxd = tr(px,py) @ rotZ(a) @ box
    drawPolyline(ax, boxd)

    ax.set_xlim([-0.1,0.3])
    ax.set_ylim([-0.1,0.1])
    ax.set_aspect('equal')
    ax.grid()
    # plt.savefig(f'{i}.png')


#mat = np.vstack([x,y,px,py,th,alpha])
#dat = mat.T


# def drawLine(ax,x0,y0,x1,y1):
#     ax.plot(np.array([x0,x1]),np.array([y0,y1]))

# for n,m in enumerate(dat[:-1,:]):
#     fig,ax = plt.subplots()
#     ax.scatter(m[0],m[1])
#     ax.scatter(m[2],m[3])
#     drawLine(ax, m[0],m[1],m[2],m[3])
#     ax.set_xlim([-0.1,0.3])
#     ax.set_ylim([-0.1,0.1])
#     ax.set_aspect('equal')
#     ax.grid()
#     plt.savefig(f'{n}.png')
