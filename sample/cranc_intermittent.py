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

h = 43


for th in np.linspace(0,2*np.pi,30):
    x = r * np.cos(th)
    y = r * np.sin(th)

    fig,ax = plt.subplots()
    
    ax.scatter(x,y)
    
    ronoji = np.array([
        [r,r,-r,-r,r],
        [h,-h,-h,h,h],
        [1,1,1,1]
        ])
    
    ax.plot(ronoji[0],ronoji[1])

    ax.set_xlim([-200,200])
    ax.set_ylim([-200,200])
    ax.set_aspect('equal')
    ax.grid()
    
    plt.show()
    
    plt.close()


class Link:
    def __init__(self,th):
        self.x = r * np.cos(th)
        self.y = r * np.sin(th)
        
        self.px = 0
        self.py = self.y
        
        self.xy1 = np.vstack((self.x,self.y,1))
        self.pxy1 = np.vstack((self.px,self.py,1))
        self.slider1 = np.array([[-r,r],[self.py,self.py],[1,1]])
        self.shaft = np.array([0,0,1])
    
    def getLinkCord(self):
        return tr(self.px, self.py)
    
    def dot(self,H):
        self.xy1 = H @ self.xy1
        self.pxy1 = H @ self.pxy1
        self.slider1 = H @ self.slider1
    
    def draw(self,ax):
        ax.scatter(self.xy1[0],self.xy1[1])
        ax.scatter(self.pxy1[0],self.pxy1[1])
        ax.plot(self.slider1[0],self.slider1[1])
        ax.scatter(self.shaft[0],self.shaft[1])




