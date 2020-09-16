from math import sqrt,ceil,floor
from sympy import sieve,isprime
N = 600851475143

primes = list(sieve.primerange(2,sqrt(N)))

for i in primes:
	if N%i==0:
		print(i)
