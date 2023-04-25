# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 04:24:21 2023

@author: luish_000
"""



import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing 


datos = pd.read_csv("Laptop_Information2.csv")
datos



"""fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)
ax1.set_title("Datos Originales")
ax1.plot(datos)
ax2.set_title("Precios")
ax2.plot(datos["MRP"], linewidth=0, marker="o", color="blue", markersize=6)
ax3.set_title("Memoria RAM")
ax3.plot(datos["RAM"], linewidth=0, marker="+", color="orange", markersize=16)
plt.show()"""



fig = plt.figure(figsize=(8, 8))
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
ax1.set_title("Precios")
ax1.plot(datos["MRP"], linewidth=0, marker="o", color="blue", markersize=6)
ax2.set_title("Calificacion Promedio")
ax2.plot(datos["Rating"], linewidth=0, marker="+", color="orange", markersize=16)
ax3.set_title("Precios")
ax3.hist(datos["MRP"], bins=100, color="blue")
ax4.set_title("Calificacion Promedio")
ax4.hist(datos["Rating"], color="orange")
plt.show()

#1. Escala en funcion del maximo y mínimo
datos_min_max = preprocessing.MinMaxScaler().fit_transform(datos)
print('Escala en funcion del maximo y mínimo')
print(datos_min_max)

#2. Normalización en función de la norma del vector
datos_normalizer = preprocessing.Normalizer().transform(datos.T)
datos_normalizer = datos_normalizer.T
# normalizado = X / raíz_cuadrada( X_1^2 + X_2^2 + X_3^2 + ...)
print('Normalización en función de la norma del vector')
print(datos_normalizer)

#3. Estandariza (desv_std = 1, media = 0)
datos_standard_scaler = preprocessing.StandardScaler().fit_transform(datos)
# estandarizado = (X - media) / std

datos_robust_scaler = preprocessing.RobustScaler().fit_transform(datos)
# estandarizado = (X - rango_intercuartílico) / std
print('Estandarizacion')
print('Estandar\tRobusto')
print(datos_standard_scaler, datos_robust_scaler)

#Comparación de métodos
# convierte vectores de numpy a DataFrames para graficarlos
datos_min_max = pd.DataFrame(datos_min_max, columns=["","Rating","No_of_ratings","Review","Size","RAM","Price","MRP"])
datos_normalizer = pd.DataFrame(datos_normalizer,columns=["","Rating","No_of_ratings","Review","Size","RAM","Price","MRP"])
datos_standard_scaler = pd.DataFrame(datos_standard_scaler,columns=["","Rating","No_of_ratings","Review","Size","RAM","Price","MRP"])
datos_robust_scaler = pd.DataFrame(datos_robust_scaler,columns=["","Rating","No_of_ratings","Review","Size","RAM","Price","MRP"])

# crea una figura con 5 subfiguras para comparar los métodos
fig = plt.figure(figsize=(15, 3))
ax1 = fig.add_subplot(1, 5, 1)
ax2 = fig.add_subplot(1, 5, 2)
ax3 = fig.add_subplot(1, 5, 3)
ax4 = fig.add_subplot(1, 5, 4)
ax5 = fig.add_subplot(1, 5, 5)

# crea y personaliza series de datos
ax1.set_title("INGRESO")
ax1.plot(datos["MRP"], linewidth=0, marker="*", color="red", markersize=4)

ax2.set_title("Min Max")
ax2.plot(datos_min_max["MRP"], linewidth=0, marker="*", color="red", markersize=4)

ax3.set_title("Normalizer")
ax3.plot(datos_normalizer["MRP"], linewidth=0, marker="*", color="red", markersize=4)
#ax3.set_ylim(0, 1)

ax4.set_title("Standard Scaler")
ax4.plot(datos_standard_scaler["MRP"], linewidth=0, marker="*", color="red", markersize=4)

ax5.set_title("Robust Scaler")
ax5.plot(datos_robust_scaler["MRP"], linewidth=0, marker="*", color="red", markersize=4)

plt.show()

# crea una figura con 5 subfiguras para mostrar histogramas
fig = plt.figure(figsize=(15, 3))
ax1 = fig.add_subplot(1, 5, 1)
ax2 = fig.add_subplot(1, 5, 2)
ax3 = fig.add_subplot(1, 5, 3)
ax4 = fig.add_subplot(1, 5, 4)
ax5 = fig.add_subplot(1, 5, 5)

# crea y personaliza series de datos de los histogramas
ax1.set_title("INGRESO")
ax1.hist(datos["Rating"], color="red", bins=100)

ax2.set_title("Min Max")
ax2.hist(datos_min_max["Rating"], color="red", bins=100)

ax3.set_title("Normalizer")
ax3.hist(datos_normalizer["Rating"], color="red", bins=100)

ax4.set_title("Standard Scaler")
ax4.hist(datos_standard_scaler["Rating"], color="red", bins=100)

ax5.set_title("Robust Scaler")
ax5.hist(datos_robust_scaler["Rating"], color="red", bins=100)

plt.show()