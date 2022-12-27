# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 16:58:48 2022

@author: ASUS
"""

import numpy as np
import random as rd
tab=[]
tab2=[]
nbre=int(input("entrer le nombre de colonne : "))
nbre2=int(input("entrer le nombre de ligne : "))
for j in range(nbre2):
    
    for i in range(nbre):
       
        a= rd.randint(0, 21)
        tab.append(a)
    tab2.append(tab)
    tab=[]
    
tab2=np.array(tab2)
print(tab2)
b= tab2[:,0:2]
print(b)