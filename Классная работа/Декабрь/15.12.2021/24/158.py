file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\24data\24-157.txt'
with open(file_name, 'r') as f:
	s = f.readline()

ans = dict()
for i in range(len(s) - 2):
	if s[i + 1] == s[i + 2]:
		if s[i] not in ans:
			ans[s[i]] = 1
		else:
			ans[s[i]] += 1

ans = list(zip(ans.keys(), ans.values()))

print(ans)
print(max(ans, key=lambda x: x[1]))
