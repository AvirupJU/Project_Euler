from math import factorial

def comb(n, r): 
  
    return (factorial(n) / (factorial(r)  
                * factorial(n - r)))


def Paths(dim):
	return comb(2*dim,dim)

print(Paths(20))