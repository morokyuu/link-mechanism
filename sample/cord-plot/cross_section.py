# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 21:41:41 2023

@author: square
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

with Image.open("shoose.png") as im:
    size = im.size
    img = np.array(im)


# fig,ax = plt.subplots()

## 10pixおきに列を取り出す　縦に圧縮したような画像になる
arr = img[10:size[1]:10,:,0]

# arr = arr[arr < 255/2.0]


# for p in pitch:
#     arr = img[p,:,:]


