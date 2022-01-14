import re


file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\Варианты\Вариант 102-2022с\24.txt'
with open(file_name, 'r') as f:
	s = f.readline().strip()

indexes = list()
for i in range(len(s)):
	if s[i] == 'D':
		indexes.append(i)

ans = 0
for i in range(len(indexes) - 2):
	ans = max(ans, indexes[i + 2] - indexes[i])
print(ans)
