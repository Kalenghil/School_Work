file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\27data\12\27-12b.txt'
with open(file_name, 'r') as f:
	amount = int(f.readline())
	nums = list(map(int, f.readlines()))


has2 = 0
has3 = 0
has6 = 0

for num in nums:
	if num % 6 == 0:
		has6 += 1
	elif num % 3 == 0:
		has3 += 1
	elif num % 2 == 0:
		has2 += 1

print((has6 * (amount - has6)) + has2 * has3 + (has6 * (has6 - 1)) // 2)
