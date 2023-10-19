# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 23:27:31 2023

@author: square
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

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

def drawLine(ax,x0,y0,x1,y1,color='blue'):
    ax.plot(np.array([x0,x1]),np.array([y0,y1]),color=color)

def drawPolyline(ax,poly,color='blue'):
    poly = poly.T
    poly = np.vstack((poly,poly[0,:]))
    for i in range(poly.shape[0]-1):
        drawLine(ax,poly[i,0],poly[i,1],poly[i+1,0],poly[i+1,1],color=color)


r = 80 
NUM = 200
h = 40

def push(cr_th, cr_y, ro_y):
    th_t1 = np.arcsin(h/r)
    th_t3 = np.arcsin(r-2*h) + np.pi/2.0

    if 0 <= cr_th and cr_th < th_t1:
        return ro_y
    elif th_t1 <= cr_th and cr_th < np.pi/2.0:
        return cr_y-h
    elif np.pi/2.0 <= cr_th and cr_th < th_t3:
        return cr_y
    elif th_t3 <= cr_th and cr_th < 3*np.pi/2.0:
        return ro_y
    

ro_y = 0
# for th in np.linspace(0,2*np.pi,30):
for th in np.linspace(0,np.pi,30):
    x = r * np.cos(th)
    y = r * np.sin(th)

    fig,ax = plt.subplots()
    
    ax.scatter(x,y)
    
    ro_y = push(th,y,ro_y)
    ax.scatter(0,ro_y)
    
    ronoji = np.array([
        [r,r,-r,-r,r],
        [h,-h,-h,h,h],
        [1,1,1,1,1]
        ])
    
    ronoji = tr(0,ro_y) @ ronoji
    
    ax.plot(ronoji[0],ronoji[1])
    
    

    ax.set_xlim([-200,200])
    ax.set_ylim([-200,200])
    ax.set_aspect('equal')
    ax.grid()
    
    plt.show()
    
    plt.close()
