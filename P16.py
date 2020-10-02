def sod(number):
	s= sum(list(map(int,str(number))))
	return s

print(sod(2**1000))