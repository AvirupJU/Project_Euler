from math import sqrt,ceil,floor
from sympy import sieve,isprime
import numpy as np
N=2000000
primes=list(sieve.primerange(2,N))
print(sum(primes))