for a in range(1, 50):
	flag = True
	for x in range(100000):
		s = (x & 105 == 0) <= ((x % 58 != 0) <= (x % a != 0))
		if s is False:
			flag = False
	if flag:
		print(a)
