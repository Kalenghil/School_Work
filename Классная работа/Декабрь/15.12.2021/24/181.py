import re

file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\24data\24-181.txt'
with open(file_name, 'r') as f:
	s = f.readline()

gap = 1
lens = list(map(lambda x: len(x), s.split('.')))
ans = list()
for i in range(len(lens) - gap):
	ans.append(sum(lens[i:i + gap + 1]) + gap)

print(max(ans))
