file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\17data\17-257.txt'
with open(file_name, 'r') as f:
	nums = list(map(int, f.readlines()))

odd, even = list(), list()
for num in nums:
	if num % 2 == 0:
		even.append(num)
	else:
		odd.append(num)

if max(even) > max(odd):
	print(len(even), min(even))
else:
	print(len(odd), min(odd))
