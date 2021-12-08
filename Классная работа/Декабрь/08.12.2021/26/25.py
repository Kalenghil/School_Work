file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\26data\26-k5.txt'
with open(file_name, 'r') as f:
	n, k, m = list(map(int, f.readline().split()))
	nums = list(map(int, f.readlines()))

nums.sort(reverse=True)
cheapest_phones = list(reversed(nums))[:k]
premium_phones = nums[:m]
print(min(premium_phones), sum(cheapest_phones) // len(cheapest_phones))