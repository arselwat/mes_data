import random as rd
import math as mt
tab=[]
taille=int(input("entrer le nombre d'element du tableau : "))
for i in range(taille):
    print("l'element ",i+1,"est :")
    x=int(input())
    tab.append(x)
print("mon tableau : ",tab)
t1=sorted(tab)
print("tableau trié :",t1)
# la moyenne

moyenne=sum(tab)/len(tab)

print("la moyenne est : ",moyenne)

#  les extremes 

print("les valeurs extremes sont ", t1[0]," et ",t1[-1])  

# etendue

e= t1[-1]-t1[0]
print("l'etendue est : ",e)

# la variance

 

# la variance
svar=0
for i in range(taille):
    svar+=(tab[i]-moyenne)**2
var=svar/(len(tab)-1)
print("la variance est : ",var)
# l'ecart type 

print("l'ecart type est ", mt.sqrt(var))
