from math import sqrt,ceil,floor
from sympy import sieve,isprime

def digsum(n): #digitsum
	ds = sum(list(map(int,str(n))))
	return ds

def perSquare(n): #generate perfect squares
	ls=[]
	for i in range(1,n+1):
		if sqrt(i)==int(sqrt(i)):
			ls.append(i)
	return ls	

def isDigit(digit,n): #gen of number with a particular digit
	ls=[]
	for i in range(n):
		if str(digit) in str(i):
			ls.append(i)
	return ls

def P1(lim):
	a= set(perSquare(lim))
	b= set(range(7,lim,7))
	return (a^b)

def P2(lim):
	a=list(sieve.primerange(2,lim))
	a1=set([i-1 for i in a])
	b=set(range(10,100))
	return(a1^b)

def P3(lim):
	a=list(perSquare(lim))
	a1=set([i-1 for i in a])
	b=set(range(100,lim+1))
	return(a1^b)

def P4(lim):
	a=set(isDigit(3,lim))
	b=set(isDigit(8,lim))
	return(a^b)

def P5(lim):
	a=set(range(11,lim,11))
	b=set([i for i in range(lim) if isprime(digsum(i))])
	return(a^b)

print(min(P1(100000)&P2(100000)&P3(100000)&P4(100000)&P5(100000)))




