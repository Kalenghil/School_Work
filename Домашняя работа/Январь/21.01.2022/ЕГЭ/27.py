from pprint import pprint
import time

start = time.time_ns()
file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\Варианты\Вариант 5-2022_ш\27B__8lrr.txt'
k = 123
rems = [[] for _ in range(k)]
with open(file_name, 'r') as f:
	amount = int(f.readline())
	for i in range(amount):
		num = int(f.readline())
		rems[num % k].append((num, i))
max_pos = 0
max_sum = 0
ans = 0
for i in range(1, k):
	for r1 in rems[i]:
		for r2 in rems[k - i]:
			if r1[0] > r2[0] and r2[1] > r1[1]:
				s = r1[0] + r2[0]
				if s > max_sum:
					ans = str(r1[0]) + str(r2[0])
					max_sum = s
					max_pos = min(r1[1], r2[1])
				elif s == max_sum:
					if min(r1[1], r2[1]) < max_pos:
						ans = str(r1[0]) + str(r2[0])
						max_sum = s
						max_pos = min(r1[1], r2[1])
print(ans, max_sum, (time.time_ns() - start) // 1000)