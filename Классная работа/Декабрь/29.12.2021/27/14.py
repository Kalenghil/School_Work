file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\27data\14\27.txt'
rems = [0] * 12
with open(file_name, 'r') as f:
	amount = int(f.readline())
	for _ in range(amount):
		num = int(f.readline())
		rems[num % 12] += 1


ans = 0
for i in range(1, 6):
	ans += rems[i] * rems[12 - i]
ans += (rems[6] * (rems[6] - 1)) // 2
ans += (rems[0] * (rems[0] - 1)) // 2
print(ans)
