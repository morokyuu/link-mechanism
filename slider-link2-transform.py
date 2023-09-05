# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:03:11 2023

@author: square
"""


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




r = 0.012
L = 0.1
Lx = 0.07
NUM = 20

th = np.linspace(0.001,np.pi*2,NUM)
x = r * np.cos(th)
y = r * np.sin(th)
alpha = np.arctan(y/Lx - x)

l = np.sqrt((Lx - x)**2 + (0 - y)**2)

px = (L - l)*np.cos(-alpha) + Lx
py = (L - l)*np.sin(-alpha)

boxpt = []
for a,x,y in zip(alpha,x,y):
    R = rotZ(a) @ tr(x,y)
    box = np.array([[r,r,-r,-r],[r,-r,r,-r],[1,1,1,1]])
    print( R @ box )
    # print(t)
    boxpt.append(R @ box)

exit()


fig,ax = plt.subplots()
ax.scatter(x,y)
ax.scatter(Lx,0)
# ax.scatter()
ax.scatter(px,py)
ax.set_aspect('equal')
ax.grid()




mat = np.vstack([x,y,px,py,th,alpha])
dat = mat.T


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
