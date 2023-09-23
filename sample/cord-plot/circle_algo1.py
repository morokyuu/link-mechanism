# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 23:11:32 2023

@author: square
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

with Image.open("shoose.png") as im:
    size = im.size
    img = np.array(im)

img = img[:,:,0]




def circle_search(R, oy,ox):
    th = np.linspace(0, 2*np.pi, 360)
    y = R * np.cos(th) + oy
    x = R * np.sin(th) + ox
    y = y.astype(int)
    x = x.astype(int)
    return y,x






y,x = circle_search(10, 302, size[0]/2)

for deg,(ty,tx) in enumerate(zip(y,x)):
    print(img[ty,tx])
    if img[ty,tx] < 100:
        print(f"{deg} tx,ty={tx},{ty}")
        break


# img[y,x] = 0

plt.imshow(img)

plt.scatter(tx,ty)

