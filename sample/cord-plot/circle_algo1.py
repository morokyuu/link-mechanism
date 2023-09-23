# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 23:11:32 2023

@author: square
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

with Image.open("sample.png") as im:
    size = im.size
    img = np.array(im)

img = img[:,:,0]




def circle_search(R, ox,oy):
    th = np.linspace(0, 2*np.pi, 360)
    x = R * np.cos(th) + ox
    y = R * np.sin(th) + oy
    x = x.astype(int)
    y = y.astype(int)
    return x,y






x,y = circle_search(10, 75, 75)

# #preview
# img[x,y] = 30
# plt.imshow(img)


for deg,(tx,ty) in enumerate(zip(x,y)):
    print(img[tx,ty])
    if img[tx,ty] < 100:
        print(deg)
        break

