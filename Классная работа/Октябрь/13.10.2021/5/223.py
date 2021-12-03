for i in range(11, 100000):
	s = bin(i)[2:]
	s = s + s[-2]
	s = s + s[1]
	if int(s, 2) > 100:
		print(i, int(s, 2))
		break
