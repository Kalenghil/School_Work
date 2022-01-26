import math
import time
from functools import lru_cache


@lru_cache(None)
def is_prime(num):
	n = -num
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
	return True


file_name = r'D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_январь\27data\88\27-88b.txt'
summ = 0
start = time.time()
sums = dict()
ans = 0
with open(file_name, 'r') as f:
	amount, k = list(map(int, f.readline().split()))
	counter = 0
	for _ in range(amount):
		num = int(f.readline())
		if num < 0:
			if is_prime(num):
				counter += 1
		summ += num
		if counter in sums:
			sums[counter].append(summ)
		else:
			sums[counter] = [summ]

ans = -math.inf
for t in range(1, counter // k):
	tk = k * t
	for i in range(counter - tk):
		a = sums[i]
		b = sums[i + tk]
		for a_elem in a:
			for b_elem in b:
				summ = b_elem - a_elem
				ans = max(ans, summ)
	print(f'gotcha {tk} {ans}')

print(k, ans)
print(f'{time.time() - start:.4f}')
