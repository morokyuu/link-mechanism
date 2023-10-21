# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:03:11 2023

@author: square
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

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


crank_r = 50 
NUM = 30
slith = 35

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
    def __init__(self,H=np.eye(3,3)):
        self.ronoji_ini = np.array([
            [crank_r,crank_r,-crank_r,-crank_r,crank_r],
            [slith,-slith,-slith,slith,slith],
            [1,1,1,1,1]
            ])
        self.ronoji = self.ronoji_ini * 1 #hard copy
        self.ro_y = 0
        self.H = H

    def _push(self, cr_y, ro_y):
        if cr_y >= ro_y + slith:
            return cr_y - slith
        elif cr_y < ro_y - slith:
            return cr_y + slith
        else:
            return ro_y

    def setPos(self,cr_y):
        self.ro_y = self._push(cr_y, self.ro_y)
        self.ronoji = self.H @ (tr(0,self.ro_y) @ self.ronoji_ini)
    
    def draw(self,ax):
        ax.plot(self.ronoji[0],self.ronoji[1])

class Shape:
    def __init__(self,H=np.eye(3,3)):
        df = pd.read_csv("foot.txt")
        self.shape_ini = np.vstack((df['x'],df['y'],np.ones(df.shape[0])))
        self.length = df['y'].max()
        self.shape_ini = tr(0,-self.length/2.0) @ self.shape_ini
        self.H = H
    
    def setPos(self,ro_y):
        self.shape = self.H @ tr(0,ro_y) @ self.shape_ini

    def draw(self,ax):
        ax.plot(self.shape[0], self.shape[1])

class Bon:
    def __init__(self):
        df = pd.read_csv("bon.txt")
        self.x = df['x']
        self.y = df['y']
        self.xy1 = np.vstack((self.x,self.y,np.ones(df['x'].shape[0])))
    
    def dot(self,H):
        self.xy1 = H @ self.xy1
    
    def draw(self,ax):
        ax.plot(self.xy1[0], self.xy1[1])


Hview = tr(0,-50)
#Hview = tr(0,0) @ rotZ(np.pi/2)
#Hview = np.eye(3)

l = Link()
#cr = Crank(rotZ(np.pi/3))
cr = Crank()
sh = Shape(tr(0,0))

ro_y = 0
for th in np.linspace(0, 2*np.pi, NUM):
    
    fig,ax = plt.subplots()
    
    cr.setPos(th)
    cr.draw(ax)
    
    l.setPos(cr.getY())
    l.draw(ax)
    
    sh.setPos(l.ro_y)
    sh.draw(ax)
#    Hl = l.getLinkCord()
#    
#    sh = Shape()
#    sh.dot(Hl @ Hview @ tr(0,-70))
#    #sh.dot(Hl @ Hview @ rotZ(-np.pi/2) @ tr(0,-70))
#    sh.draw(ax)
    
#    bon_tilt = rotZ(np.cos(th*10)*0.1)
#    
#    bon = Bon()
#    bon.dot(Hview @ bon_tilt @ tr(0,20))
#    bon.draw(ax)
    
    ax.set_xlim([-200,200])
    ax.set_ylim([-200,200])
    ax.set_aspect('equal')
    ax.grid()
    
    plt.show()
    
    plt.close()


sys.exit()




