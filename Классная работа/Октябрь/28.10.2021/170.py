def max_divisors_difference(num):
	for i in range(2, int(num ** 0.5) + 2):
		if num % i == 0:
			max_divisor = num // i
			return max_divisor - i
	return 0


for num in range(350_001, 360_001):
	diff = max_divisors_difference(num)
	if diff % 23 == 9:
		print(num, diff)
