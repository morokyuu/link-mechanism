# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 23:11:32 2023

@author: square
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("foot.txt",sep="\t")

fig,ax = plt.subplots()

ax.plot(df['x'],df['y'])



