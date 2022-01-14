def return_divs(n):
	mult = 1
	counter = 0
	root = int(n**0.5) + 2
	for i in range(2, n // 2):
		if i > root and counter == 0:
			break
		else:
			if counter < 5 and mult * i < n:
				if n % i == 0:
					print(i, end=' ')
					mult *= i
					counter += 1
			else:
				break
	return mult if counter == 5 else 0


for i in range(500_000_001, 500_001_000):
	mult = return_divs(i)
	print(i, mult)