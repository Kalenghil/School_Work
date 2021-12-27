file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\27data\9\27-9b.txt'
nums = list()
with open(file_name, 'r') as f:
	amount = int(f.readline())
	for i in range(amount):
		nums.append((i, int(f.readline())))


nums.sort(key=lambda x: x[1])
nums = list(filter(lambda x: x[1] % 2 == 1, nums))

flag = False
for i in range(amount - 1):
	if flag:
		break
	for j in range(i + 1, amount):
		dist = abs(nums[j][0] - nums[i][0])
		if dist >= 6:
			print(nums[i][1] * nums[j][1])
			flag = True
			break
