import math, itertools
from sympy import divisor_count
def triangle():
	triangle = 0
	for i in itertools.count(1):
		triangle += i  # This is the ith triangle number, i.e. num = 1 + 2 + ... + i = i * (i + 1) / 2
		if divisor_count(triangle) > 500:
			print(str(triangle))
			return

triangle()