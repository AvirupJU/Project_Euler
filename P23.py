def compute():
	upper = 28124
	divisorsum = [0] * upper
	for i in range(1, upper):
		for j in range(i * 2, upper, i):
			divisorsum[j] += i
	abundant = [i for (i, x) in enumerate(divisorsum) if x > i]
	
	nonAb = [False] * upper
	for i in abundant:
		for j in abundant:
			if i + j < upper:
				nonAb[i + j] = True
			else:
				break
	
	ans = sum(i for (i, x) in enumerate(nonAb) if not x)
	return str(ans)


if __name__ == "__main__":
	print(compute())