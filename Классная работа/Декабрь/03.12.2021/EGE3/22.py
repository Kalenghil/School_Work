for i in range(1, 1000):
	x = i
	l = 0
	m = 0
	while x > 0:
		if x % 2 == 0:
			l += 1
		else:
			m += x % 6
		x //= 6
	if l == 2 and m == 5:
		print(i)
