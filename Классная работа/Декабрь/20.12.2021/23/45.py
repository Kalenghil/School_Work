def func(start, end):
	if start == end:
		return 1
	if start > end:
		return 0
	return func(start + 1, end) + func(start + 3, end) + func(start * 2, end)


print(func(4, 10) * func(10, 20))
