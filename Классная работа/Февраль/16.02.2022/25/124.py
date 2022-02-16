import time


start = time.time()
def isPrime(num):
	for i in range(2, int(num ** 0.5) + 1):
		if num % i == 0:
			return False
	return True


def make_prime_list(num):
	primes = list()
	for i in range(2, num + 1):
		if isPrime(i):
			primes.append(i)
	return primes


primes_list = make_prime_list(604298 // 2 // 3)
print(f'{time.time() - start:.2f}')
print(len(primes_list))

ans = list()
for i in range(len(primes_list) - 2):
	for j in range(i, len(primes_list) - 1):
		for k in range(j, len(primes_list)):
			if i != j != k:
				a, b, c = primes_list[i], primes_list[j], primes_list[k]
				num = a * b * c
				if 536792 <= num <= 604298:
					ans.append(num)
print(f'{time.time() - start:.2f}')