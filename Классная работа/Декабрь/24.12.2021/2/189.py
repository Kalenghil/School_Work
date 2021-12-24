for x in range(2):
	for y in range(2):
		for z in range(2):
			for w in range(2):
				s = int((x and z) or ((w <= x) == (z <= y)))
				if s == 0:
					print(f'x: {x}, y: {y}, z: {z}, w: {w}: {s}')
