# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:03:11 2023

@author: square
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys


SAVEFIG = False
# SAVEFIG = True
crank_r = 77
NUM = 30

#right-hand-sys
def rotZ(th):
    return np.array([
        [ np.cos(th),-np.sin(th), 0.0],
        [ np.sin(th), np.cos(th), 0.0],
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

def drawLine(ax,x0,y0,x1,y1,color='blue'):
    ax.plot(np.array([x0,x1]),np.array([y0,y1]),color=color)

def drawPolyline(ax,poly,color='blue'):
    poly = poly.T
    poly = np.vstack((poly,poly[0,:]))
    for i in range(poly.shape[0]-1):
        drawLine(ax,poly[i,0],poly[i,1],poly[i+1,0],poly[i+1,1],color=color)



class Crank:
    def __init__(self,H=np.eye(3,3)):
        self.xy_ini = np.array([[crank_r],[0],[1]])
        self.xy_cr = self.xy_ini * 1 #hard copy
        self.H = H

    def setPos(self,th):
        self.xy_cr = self.H @ rotZ(th) @ self.xy_ini
        self.shaft = self.H @ np.array([0,0,1])

    def getY(self):
        return self.xy_cr[1,0]

    def draw(self,ax):
        ax.scatter(self.xy_cr[0],self.xy_cr[1])
        ax.scatter(self.shaft[0],self.shaft[1])

class Link:
    def __init__(self,slith,H=np.eye(3,3)):
        self.slith = slith
        self.ronoji_ini = np.array([
            [crank_r,crank_r,-crank_r,-crank_r,crank_r],
            [self.slith,-self.slith,-self.slith,self.slith,self.slith],
            [1,1,1,1,1]
            ])
        self.ronoji = self.ronoji_ini * 1 #hard copy
        self.ro_y = 0
        self.H = H

    def _push(self, cr_y, ro_y):
        if cr_y >= ro_y + self.slith:
            return cr_y - self.slith
        elif cr_y < ro_y - self.slith:
            return cr_y + self.slith
        else:
            return ro_y

    def setPos(self,cr_y):
        self.ro_y = self._push(cr_y, self.ro_y)
        self.ronoji = self.H @ (tr(0,self.ro_y) @ self.ronoji_ini)
    
    def draw(self,ax):
        ax.plot(self.ronoji[0],self.ronoji[1])

class Shape:
    def __init__(self,size=24.0,bon_length=100,H=np.eye(3,3)):
        df = pd.read_csv("foot.txt")
        DATA_FOOTSIZE = 24.0
        self.fscale = size/DATA_FOOTSIZE
        self.shape_ini = np.vstack((df['x'],df['y'],np.ones(df.shape[0])))
        self.length = df['y'].max() * self.fscale
        self.shape_ini = tr(0,-self.length/2.0) @ scale(self.fscale) @ self.shape_ini
        self.bon_length = bon_length
        self.H = H
    
    def setPos(self,ro_y):
        self.shape = self.H @ tr(0,ro_y) @ self.shape_ini

    def getSlitHeight(self):
        return crank_r - (self.length - self.bon_length)/2.0

    def draw(self,ax):
        ax.plot(self.shape[0], self.shape[1])

class Bon:
    def __init__(self,H=np.eye(3,3)):
        df = pd.read_csv("bon.txt")
        self.shape_ini = np.vstack((df['x'],df['y'],np.ones(df.shape[0])))
        self.length = df['y'].max()
        self.shape = self.shape_ini * 1 # hard copy
        self.H = H

    def setPos(self,th):
        self.shape = self.H @ rotZ(0.1*np.sin(th*3)) @ self.shape_ini
    
    def draw(self,ax):
        ax.plot(self.shape[0], self.shape[1])



bon = Bon(tr(0,-50))
sh = Shape(20,bon.length,tr(0,0))
slith = sh.getSlitHeight()
l = Link(slith+15) #if bon overrun on border of shape, add some value to slith.
cr = Crank(rotZ(np.arctan(slith/crank_r)))

ro_y = 0
for n,th in enumerate(np.linspace(0, 2*np.pi, NUM)):
    
    fig,ax = plt.subplots()
    
    cr.setPos(th)
    cr.draw(ax)
    
    l.setPos(cr.getY())
    l.draw(ax)
    
    sh.setPos(l.ro_y)
    sh.draw(ax)

    bon.setPos(th)
    bon.draw(ax)

    ax.set_xlim([-200,200])
    ax.set_ylim([-200,200])
    ax.set_aspect('equal')
    ax.grid()
    
    if SAVEFIG:
        plt.savefig(f"anim/{n}.png")
    else:
        plt.show()
    
    plt.close()


sys.exit()




