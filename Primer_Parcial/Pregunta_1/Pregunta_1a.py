# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 08:24:21 2023

@author: luish_000
"""

import numpy as np
import pandas as pd
from math import sqrt

def media (lista):          #Funcion para la calcular la MEDIA
    suma = 0
    for valor in lista:
        suma += valor
    
    return suma / len(lista)

def mediana (lista):        #Función para crear la MEDIANA
    lista.sort()
    if len(lista) % 2 != 0:
        middle = int ((len(lista) - 1) / 2)
        return lista[middle]
    elif len (lista) % 2 == 0:
        middle_1 = int(len(lista) / 2)
        middle_2 = int(len(lista) / 2) - 1
        return media([lista[middle_1], lista[middle_2]])

def desviacion_estandar (lista, valor_media):   #Función para crear la 
    suma = 0                                    #DESVIACION ESTANDAR
    
    for valor in lista:
        suma += (valor - valor_media) ** 2
    
    fraccion = suma / (len(lista))
    
    return sqrt(fraccion)

def moda (lista):
    cont = 0
    mayor = 0
    n = len(lista)
    for i in range(n):
        cont = 0
        for j in range(n):
            if(lista[i] == lista[j]):
                cont = cont + 1
        if (cont > mayor):
            mayor = cont
            mod = lista[i]
    return mod

def cuartil(lista):
    lista.sort()
    mini = lista[0]
    maxi = lista[len(lista) - 1]
    
    quartil = int(len(lista) / 4)
    print("\tCuartil: Min: ", mini, " Q1: ", lista[quartil], " Q2: ", lista[2 * quartil],
          "Q3: ", lista[3* quartil], "Max: ", maxi)
    
    
dataset = pd.read_csv("Laptop_Information.csv")  #Leemos el dataset Heart.csv

x1 = dataset["Rating"].tolist()        #Calificacion Promedio 0 - 5
x2 = dataset["No_of_ratings"].tolist() #Total de calificaciones de lo usuarios
x3 = dataset["Review"].tolist()        #Total de opiniones de los usuarios
x4 = dataset["Size"].tolist()          #Tamaño de la pantalla de la laptop
x5 = dataset["RAM"].tolist()           #Cantidad de memoria RAM
x6 = dataset["MRP"].tolist()         #Precio de la computadora portatil

print("-----DATOS ESTADÍSTICOS-----")
print('CALIFICACION PROMEDIO DE LA LAPTOP')
print("\tMedia:               ", media(x1))
print("\tMediana:             " , mediana(x1))
print("\tModa:                " , moda(x1))
cuartil(x1)
print("\tDesviación Estandar: ", desviacion_estandar(x1, media(x1)))
print("**********************************************************************")
print()
print('NUMERO TOTAL DE CALIFICACIONES')
print("\tMedia:               ", media(x2))
print("\tMediana:             " , mediana(x2))
print("\tModa:                " , moda(x2))
print("\tDesviación Estandar: ", desviacion_estandar(x2, media(x2)))
print("**********************************************************************")
print()
print('NUMERO TOTAL DE OPINIONES DE USUARIOS')
print("\tMedia:               ", media(x3))
print("\tMediana:             " , mediana(x3))
print("\tModa:                " , moda(x3))
print("\tDesviación Estandar: ", desviacion_estandar(x3, media(x3)))
print("**********************************************************************")
print()
print('TAMAÑO DE LA PANTALLA EN cm')
print("\tMedia:               ", media(x4))
print("\tMediana:             " , mediana(x4))
print("\tModa:                " , moda(x4))
print("\tDesviación Estandar: ", desviacion_estandar(x4, media(x4)))
print("**********************************************************************")
print()
print('CANTIDAD DE MEMORIA RAM')
print("\tMedia:               ", media(x5))
print("\tMediana:             " , mediana(x5))
print("\tModa:                " , moda(x5))
cuartil(x5)
print("\tDesviación Estandar: ", desviacion_estandar(x5, media(x5)))
print("**********************************************************************")
print()
print('PRECIO DE LA LAPTOP')
print("\tMedia:               ", media(x6))
print("\tMediana:             ", mediana(x6))
print("\tModa:                ", moda(x6))
cuartil(x6)
print("\tDesviación Estandar: ", desviacion_estandar(x6, media(x6)))
print("**********************************************************************")
print()





