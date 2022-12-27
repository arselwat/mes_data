import numpy as np

print("creation d'une matrice ")
liste=[]
matrice=[]
l= int (input("entrer le nombre de lignes : "))
c= int (input("entrer le nombre de colonnes : "))
for i  in range(l):
    for j in range(c):
        print("element ",j," : ")
        
        a= input()
        liste.append(a)
    matrice.append(liste)
    liste=[]
print(matrice)
tableau= np.array(matrice)
print(tableau)
print("dimension : ",tableau.shape)
print("nombre d'element : ",tableau.size)
print("type : ",np.dtype(tableau))
