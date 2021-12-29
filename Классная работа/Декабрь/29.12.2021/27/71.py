import math

file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\27data\71\27-71b.txt'
with open(file_name, 'r') as f:
	amount = int(f.readline())
	nums = list(map(int, f.readlines()))


max_sum = -math.inf
min_len = 0
for i in range(amount):
	summ = nums[i]
	cur_len = 1
	for j in range(i + 1, amount):
		if summ % 69 == 0:
			break
		summ += nums[j]
		cur_len += 1
	if summ % 69 == 0 and (summ > max_sum or (max_sum == summ and cur_len < min_len)):
		max_sum = summ
		min_len = cur_len

print(min_len)
