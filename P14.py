import math
import sys
'''
recursive method
def collatz(x):
	if x == 1:
		return 1
	if x % 2 == 0:
		y = x // 2
	else:
		y = x * 3 + 1
	return collatz(y) + 1
'''

def collatz(number):
	i=1
	while(number>1):
		if number%2==0:
			number//=2
			i+=1
		else:
			number=3*number+1
			i+=1
	return i

def compute():
	#sys.setrecursionlimit(3000)
	ans = max(range(1, 1000000), key=collatz)
	return str(ans)

print(compute())

