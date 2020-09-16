from math import sqrt
import numpy as np 
N=100000
for i in range(1,N):
	for j in range(i,N):
		if i+j+sqrt(i**2 +j**2)==1000:
			print(i,j)
			break;