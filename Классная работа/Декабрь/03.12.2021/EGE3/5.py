for i in range(10000, 100_000):
	a, b, c, d, e = list(map(int, str(i)))
	sums = sorted((a ** 2 + c ** 2 + e ** 2, b ** 2 + d ** 2))
	if sums[0] == 59 and sums[1] == 81:
		print(i)
