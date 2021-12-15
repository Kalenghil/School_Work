file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\24data\24-s1.txt'
with open(file_name, 'r') as f:
	strings = list(map(lambda x: x.strip(), f.readlines()))

strings = list(map(lambda x: (x, x.count('A')), strings))
idx = strings.index(min(strings, key=lambda x: x[1]))

ans = dict()
for letter in strings[idx][0]:
	if letter not in ans:
		ans[letter] = 1
	else:
		ans[letter] += 1

ans = list(zip(ans.keys(), ans.values()))

ans.sort(key=lambda x: x[0], reverse=True)
max_letter = max(ans, key=lambda x: x[1])[0]
print(ans)

ans = dict()
for string in strings:
	for letter in string[0]:
		if letter not in ans:
			ans[letter] = 1
		else:
			ans[letter] += 1
print(f'{max_letter}: {ans[max_letter]}')
