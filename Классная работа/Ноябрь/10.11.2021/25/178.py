def divisors_ends_with_8(num):
	divisors = list()
	for i in range(9, int(num ** 0.5) + 2):
		if num % i == 0:
			if i % 10 == 8:
				divisors.append(i)
			elif (num // i) % 10 == 8:
				divisors.append((num // i))
	return divisors


for i in range(500_001, 505_001):
	divisors = divisors_ends_with_8(i)
	if len(divisors) != 0:
		min_divisor = min(divisors)
		print(i, min_divisor)
