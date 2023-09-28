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
row_num = np.arange(50,size[1],10)
arr = np.array([img[a,:,0] for a in row_num])


pos = []
for r,ar in enumerate(arr):
    left, right = 0,0
    # print(f"row={r}")
    for i,a in enumerate(ar):
        if a < 100:
            left = i
            break
    
    for i in range(ar.shape[0]-1,-1,-1):
        if ar[i] < 100:
            right = i
            break
    
    # print(f'left,right = {left},{right}')
    print(f'{left},{r*10}')
    print(f'{right},{r*10}')
            
            



# for p in pitch:
#     arr = img[p,:,:]


