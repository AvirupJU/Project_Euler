import itertools

def compute():
	DIGITS = 1000
	prev = 1
	cur = 0
	for i in itertools.count():
		
		if len(str(cur)) > DIGITS:
			raise RuntimeError("Not found")
		elif len(str(cur)) == DIGITS:
			return str(i)
		
		prev, cur = cur, prev + cur

print(compute())

'''
Hit and try method :=
Because the target number is relatively small, we simply compute each Fibonacci number starting
from the beginning until we encounter one with exactly 1000 digits. The Fibonacci sequence grows
exponentially with a base of about 1.618, so the numbers in base 10 will lengthen by one digit
after every log10(1.618) ~= 4.78 steps on average. This means the answer is at index around 4780.
'''