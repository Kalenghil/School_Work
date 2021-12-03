for x in range(2):
	for y in range(2):
		for z in range(2):
			ans = int(((y and z) or (z == x)))
			print(f'x:{x}; y:{y}; z:{z}; f{ans}')