# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 21:54:31 2023

@author: square
"""

import numpy as np
import matplotlib.pyplot as plt

r = 0.03
L = 0.1
NUM = 20

th = np.linspace(0.001,np.pi*2,NUM)
x = r * np.cos(th)
y = r * np.sin(th)
alpha = np.sin(th) / L

xl = L + x
yl = np.zeros((1,NUM))

# fig,ax = plt.subplots()
# ax.scatter(x,y)
# ax.scatter(xl,yl)
# ax.set_aspect('equal')
# ax.grid()

mat = np.vstack([x,y,xl,yl,th,alpha])
dat = mat.T


def drawLine(ax,x0,y0,x1,y1):
    ax.plot(np.array([x0,x1]),np.array([y0,y1]))

for n,m in enumerate(dat[:-1,:]):
    fig,ax = plt.subplots()
    ax.scatter(m[0],m[1])
    ax.scatter(m[2],m[3])
    drawLine(ax, m[0],m[1],m[2],m[3])
    ax.set_xlim([-0.1,0.3])
    ax.set_ylim([-0.1,0.1])
    ax.set_aspect('equal')
    ax.grid()
    plt.savefig(f'{n}.png')


