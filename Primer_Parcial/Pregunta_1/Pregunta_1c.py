# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:24:21 2023

@author: luish_000
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing 


datos = pd.read_csv("Laptop_Information.csv")
datos



fig = plt.figure(figsize=(8, 8))
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

ax1.set_title("Marca de Laptop")
ax1.plot(datos["Company"], linewidth=0, marker="o", color="blue", markersize=6)
ax2.set_title("Precios")
ax2.plot(datos["MRP"], linewidth=0, marker="+", color="orange", markersize=16)
ax3.set_title("Marca de Laptop")
ax3.hist(datos["Company"], bins=100, color="blue")
ax4.set_title("Precios")
ax4.hist(datos["MRP"], color="orange")
plt.show()


