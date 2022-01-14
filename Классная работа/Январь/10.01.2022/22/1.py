for i in range(1, 100000):
	x = i
	L = 0
	M = 0
	while x > 0:
		L = L + 1
		M = M + (x % 10)
		x //= 10
	if L == 3 and M == 7:
		print(i)
