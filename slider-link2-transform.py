# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:03:11 2023

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


r = 60 
NUM = 30

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

class Shape:
    def __init__(self):
        df = pd.read_csv("foot.txt")
        self.x = df['x']
        self.y = df['y']
        self.xy1 = np.vstack((self.x,self.y,np.ones(df['x'].shape[0])))
    
    def dot(self,H):
        self.xy1 = H @ self.xy1
    
    def draw(self,ax):
        ax.plot(self.xy1[0], self.xy1[1])

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


for th in np.linspace(0, np.pi*5, NUM):
    
    fig,ax = plt.subplots()
    
    l = Link(th)
    l.dot(Hview)
    l.draw(ax)
    
    Hl = l.getLinkCord()
    
    sh = Shape()
    sh.dot(Hl @ Hview @ tr(0,-70))
    #sh.dot(Hl @ Hview @ rotZ(-np.pi/2) @ tr(0,-70))
    sh.draw(ax)
    
    bon = Bon()
    bon.dot(Hview @ tr(0,20))
    bon.draw(ax)
    
    ax.set_xlim([-200,200])
    ax.set_ylim([-200,200])
    ax.set_aspect('equal')
    ax.grid()
    
    plt.show()
    
    plt.close()


sys.exit()




