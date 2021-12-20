def func(start, end):
	if start == end:
		return 1
	if start > end:
		return 0
	return func(start + 3, end) + func(start * 3, end)


print(func(5, 27))
