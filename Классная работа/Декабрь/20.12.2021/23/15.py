from functools import lru_cache


@lru_cache(None)
def func(start, end):
	if start == end:
		return 1
	if start > end:
		return 0
	return func(start + 1, end) + func(start + 3, end) + func(start * 2, end)


print(func(3, 15))
