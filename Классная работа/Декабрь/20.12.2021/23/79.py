def func(start, end):
	if start == end:
		return 1
	if start > end or start == 20:
		return 0
	return func(start + 1, end) + func(start * 2, end) + func(start * 3, end)


print(func(2, 25))
