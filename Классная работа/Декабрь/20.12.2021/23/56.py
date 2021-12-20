def func(start, end):
	if start == end:
		return 1
	if start > end or start == 28:
		return 0
	return func(start + 1, end) + func(start * 2, end)


print(func(2, 10) * func(10, 34))
