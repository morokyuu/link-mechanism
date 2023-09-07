# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 22:06:31 2023

@author: square
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame()

df["time"] = np.linspace(0,1,20)
df["x"] = 0.03 * df["time"]
df["y"] = -1/2.0 * 0.5 * df["time"]**2


fig,ax = plt.subplots()
ax.scatter(df["x"],df["y"])


