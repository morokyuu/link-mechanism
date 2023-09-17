# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 21:54:31 2023

@author: square
"""

import numpy as np
import matplotlib.pyplot as plt
import sys

r = 30
L = 250
Lx = 90

NUM = 50

th = np.linspace(0.001,np.pi*2,NUM)
x = r * np.cos(th)
y = r * np.sin(th)
alpha = np.arctan(y/(Lx - x))

l = np.sqrt((Lx - x)**2 + (0 - y)**2)

px = (L - l)*np.cos(-alpha) + Lx
py = (L - l)*np.sin(-alpha)


fig,ax = plt.subplots()
ax.scatter(x,y)
ax.scatter(Lx,0)
ax.scatter(px,py)
ax.set_aspect('equal')
ax.grid()

sys.exit()


mat = np.vstack([x,y,px,py,th,alpha])
dat = mat.T


def drawLine(ax,x0,y0,x1,y1):
    ax.plot(np.array([x0,x1]),np.array([y0,y1]))

for n,m in enumerate(dat[:-1,:]):
    fig,ax = plt.subplots()
    ax.scatter(m[0],m[1])
    ax.scatter(m[2],m[3])
    ax.scatter(Lx,0)
    drawLine(ax, m[0],m[1],m[2],m[3])
    ax.set_xlim([-200,400])
    ax.set_ylim([-200,200])
    ax.set_aspect('equal')
    ax.grid()
    # plt.savefig(f'{n}.png')


