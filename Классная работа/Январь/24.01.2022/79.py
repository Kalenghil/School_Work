import time

start = time.time()
def is_prime(num):
	for i in range(2, int(num ** 0.5) + 1):
		if num % i == 0:
			return True
	return False


counter = 0
for i in range(2, 3_557_001):
	if is_prime(i) is True:
		counter += 1
print(counter, f'{time.time() - start:.2f}')
