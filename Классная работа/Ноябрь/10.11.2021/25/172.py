def divs_amount_and_sum(num):
	counter = 2
	summ = 0
	for i in range(2, int(num ** 0.5) + 1):
		if num % i == 0:
			if i * i == num:
				counter += 1
				summ += i
			else:
				counter += 2
				summ += i + num // i
	return counter, summ


for i in range(550_000, 555_000):
	am, summ = divs_amount_and_sum(i)
	mean = int(summ / am)
	if mean % 31 == 13:
		print(i, mean)
