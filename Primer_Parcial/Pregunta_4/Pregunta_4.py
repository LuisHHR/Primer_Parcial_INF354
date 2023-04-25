# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 23:27:52 2021

@author: luish_000
"""
# Clasificación Familiar de acuerdo a mi Luis Hector
#   Abuelo: Santiago
#   Padre: Sabio
#   Madre: Ana
#   Hermana: Vanesa
#   Tio: Tito
#   Primo: Daner
#   Prima: Karen

from kanren import Relation, facts, run, eq, membero, var, lall
x = var()
parent = Relation()
facts(parent, ("Sabio", "Luis Hector"),
              ("Sabio", "Vanesa"),
              ("Santiago", "Sabio" ),
              ("Santiago", "Tito"),
              ("Tito", "Daner"),
              ("Tito", "Karen"),
              ("Ana", "Luis Hector"),
              ("Ana", "Vanesa"))

#Relación de padres
print(run(1, x, parent(x, "Luis Hector")))
print(run(2, x, parent("Sabio", x)))
print(run(2, x, parent("Tito", x)))
print(run(2, x, parent("Santiago", x)))


#Definiendo relación del abuelo
print('Abuelo de Luis Hector es: ')
abuelo, parent1 = var(), var()
print(run(1, abuelo, parent(abuelo, parent1),
                     parent(parent1, "Luis Hector")))

#Definiendo los nietos del Abuelo
print('Los nietos de Santiago son: ')
nieto, parent1 = var(), var()
print(run(4, nieto, parent("Santiago", parent1),
                     parent(parent1, nieto)))





