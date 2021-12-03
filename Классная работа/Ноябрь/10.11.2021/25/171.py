def simple_divisors_list(num):
	divisors = list()
	temp = num
	for i in range(2, int(num ** 0.5) + 2):
		if num % i == 0:
			while temp % i == 0:
				temp = temp // i
			divisors.append(i)
		if temp == 1:
			return divisors
		if len(divisors) == 0:
			return 0


for i in range(450_000, 455_000):
	divisors_list = simple_divisors_list(i)
	if divisors_list != 0 and divisors_list is not None:
		max_divisor, min_divisor = divisors_list[-1], divisors_list[0]
		if (max_divisor - min_divisor) % 29 == 11:
			print(i, max_divisor - min_divisor)
