for x in range(2):
	for y in range(2):
		for z in range(2):
			s = int((y or z) <= (not x and y))
			if s == 1:
				print(x, y, z)
