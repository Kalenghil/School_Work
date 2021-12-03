for i in range(1, 10000):
	d = i
	n = 7
	s = 13
	while s < 915:
		s = s + d
		n = n + 27
	if n == 466:
		print(i)
