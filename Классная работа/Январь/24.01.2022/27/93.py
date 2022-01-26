import math
import time


file_name = r'D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_январь\27data\93\27-93b.txt'
summ = 0
start = time.time()
sums = dict()
with open(file_name, 'r') as f:
	amount, k = list(map(int, f.readline().split()))
	counter = 0
	for _ in range(amount):
		num = int(f.readline())
		summ += num
		if num < 0 and str(num)[-1] == '3':
			counter += 1
		if counter in sums:
			sums[counter].append(summ)
		else:
			sums[counter] = [summ]

ans = -math.inf
for i in range(counter - k):
	a = sums[i]
	b = sums[i + k]
	for a_elem in a:
		for b_elem in b:
			summ = b_elem - a_elem
			ans = max(ans, summ)

print(ans)
print(k)
print(f'{time.time() - start:.4f}')
