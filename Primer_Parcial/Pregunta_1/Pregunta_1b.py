# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 10:45:28 2023

@author: luish_000
"""

import numpy as np
import pandas as pd
import statistics as stat
import matplotlib.pyplot as plt

dataset = pd.read_csv("Laptop_Information.csv")  #Leemos el dataset Heart.csv

x1 = dataset["Rating"].tolist()        #Calificacion Promedio 0 - 5
x2 = dataset["No_of_ratings"].tolist() #Total de calificaciones de lo usuarios
x3 = dataset["Review"].tolist()        #Total de opiniones de los usuarios
x4 = dataset["Size"].tolist()          #Tamaño de la pantalla de la laptop
x5 = dataset["RAM"].tolist()           #Cantidad de memoria RAM
x6 = dataset["MRP"].tolist()         #Precio de la computadora portatil

print("-----DATOS ESTADÍSTICOS-----")
print('CALIFICACION PROMEDIO DE LA LAPTOP')
print("\tMedia:               ", np.mean(x1))
print("\tMediana:             ", np.median(x1))
print("\tModa:                ", stat.mode(x1))
print("\tDesviación Estandar: ", np.std(x1))
print("**********************************************************************")
print()
print('NUMERO TOTAL DE CALIFICACIONES')
print("\tMedia:               ", np.mean(x2))
print("\tMediana:             ", np.median(x2))
print("\tModa:                ", stat.mode(x2))
print("\tDesviación Estandar: ", np.std(x2))
print("**********************************************************************")
print()
print('NUMERO TOTAL DE OPINIONES DE USUARIOS')
print("\tMedia:               ", np.mean(x3))
print("\tMediana:             ", np.median(x3))
print("\tModa:                ", stat.mode(x3))
print("\tDesviación Estandar: ", np.std(x3))
print("**********************************************************************")
print()
print('TAMAÑO DE LA PANTALLA EN cm')
print("\tMedia:               ", np.mean(x4))
print("\tMediana:             ", np.median(x4))
print("\tModa:                ", stat.mode(x4))
print("\tDesviación Estandar: ", np.std(x4))
print("**********************************************************************")
print()
print('CANTIDAD DE MEMORIA RAM')
print("\tMedia:               ", np.mean(x5))
print("\tMediana:             ", np.median(x5))
print("\tModa:                ", stat.mode(x5))
print("\tDesviación Estandar: ", np.std(x5))
print("**********************************************************************")
print()
print('PRECIO DE LA LAPTOP')
print("\tMedia:               ", np.mean(x6))
print("\tMediana:             ", np.median(x6))
print("\tModa:                ", stat.mode(x6))
print("\tDesviación Estandar: ", np.std(x6))
print("**********************************************************************")
print()

print(np.quantile(x1, [0, 1/4, 1/2, 3/4, 1]))
cuantiles = [(2, "Mediana"),
             (3, "Terciles"),
             (4, "Cuartiles")]
#             (5, "Quintiles"),
#            (10, "Deciles"),
#            (100, "Percentiles")]

cortes = []
for cuantil in cuantiles:
    corte = []
    valor = 0
    for i in range(cuantil[0]-1):
        valor += 1/cuantil[0]
        corte.append(valor)         
    cortes.append(corte)

for i in range(len(cuantiles)):
    plt.figure(figsize=(7.5, 5))
    plt.title(cuantiles[i][1], size=22)
    plt.ylabel("Frecuencia", size=16)
    plt.xlabel("Calificación 0 - 5", size=20)
    plt.hist(x1, 100, label="Rating", color="pink")
    #print(np.quantile(x1, [0] + cortes[i] + [1]))
    for corte in cortes[i]:
        plt.axvline(x = np.quantile(x1, corte), label="%.2f" % corte, linewidth=2)
    if i < len(cuantiles) - 1:
        plt.legend()
    plt.show()
    print("\n"*4)

