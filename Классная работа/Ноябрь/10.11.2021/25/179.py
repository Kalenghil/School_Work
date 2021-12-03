def divs_diff(num):
	for i in range(2, int(num ** 0.5) + 1):
		if num % i == 0:
			return num // i - i
	return 0


for i in range(800_001, 805_001):
	diff = divs_diff(i)
	if diff != 0 and diff % 138 == 0:
		print(i, diff)
