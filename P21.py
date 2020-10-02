#Amicable
import numpy as np
n=10000
liste=np.zeros(n)
for i in range(n):
    for j in range(1,i):
        if i%j==0:
            liste[i]+=j
son=[]
for i in range(n):
    x=int(liste[i])
    if liste[i]<n:
        if i==liste[x] and i!=x:
            son.append(liste[i])
print(sum(son))