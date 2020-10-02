import math
from sympy import sieve,isprime

s=0
pr_max=40
while abs(1-2*s)<1000 and abs(s**2-s+41)<1000:
	s+=1
	pr_max+=s
product = (1-2*s)*(s**2-s+41)
print(product," ",pr_max)
'''
c=0
for i in range(0,46):
	p=(i-5)**2+(i-5)+41
	#print(p," ")
	if isprime(p):
		c+=1
print("//",c)
'''