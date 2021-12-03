file_path = r'D:\МАТЕРИАЛЫ\ЕГЭ\Варианты\Вариант 4-2022_ш\27B__7nx8.txt'

with open(file_path, 'r') as f:
	n, a, b = map(int, f.readlines())

print(n, a, b)
summ = 0
diff = b - a
fst = b - (b // diff) * diff
tmp = fst
for i in range(2, n):
	tmp += diff
	if i % 2 == 0:
		summ += tmp

print(summ)
