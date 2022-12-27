# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:45:33 2022

@author: ASUS
"""
import numpy as np
import random as rd
import math as mt
tab=[]
taille=int(input("entrer le nombre d'element du tableau : "))
for i in range(taille):
    x=rd.randint(0, 20)
    tab.append(x)
print("population: ",tab)


t1= []
for i in range(15,35):
    t1.append(tab[i])

print("echantillon : ",t1)

print("la moyenne de la population est ",sum(tab)/len(tab))
print("la moyenne de l'echantillon est ",sum(t1)/len(t1))
svar=0
for i in range(len(t1)):
    svar+=(tab[i]-sum(t1)/len(t1))**2
var=svar/(len(tab)-1)
print("la variance de l'echant. est : ",var)
# l'ecart type 

print("l'ecart type de l'echant. est  ", mt.sqrt(var))
