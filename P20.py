import math
def digsum(n): #digitsum
	ds = sum(list(map(int,str(n))))
	return ds

print(digsum(math.factorial(100)))