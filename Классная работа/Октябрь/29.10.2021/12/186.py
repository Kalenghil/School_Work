s = '7' * 143
while '777' in s:
	s = s.replace('777', '22', 1)
	s = s.replace('222', '7', 1)
print(s)
