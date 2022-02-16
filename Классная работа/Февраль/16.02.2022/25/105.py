def isPrime(num):
	for i in range(2, int(num ** 0.5) + 1):
		if num % i == 0:
			return False
	return True


def fstPrimeDiv(num):
	for i in range(2, int(num ** 0.5) + 1):
		if num % i == 0:
			if isPrime(i) and isPrime(num // i):
				return i, True
	return 1, False


ans = list()
for i in range(523_456, 578_926):
	div, res = fstPrimeDiv(i)
	if res and div != i // div:
		ans.append((i, (i // div) - div))


print(min(ans, key=lambda x: x[1]))
