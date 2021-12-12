file_name = r'C:\Users\Bosnian\Desktop\School_Work\Материалы\26data\26-k5.txt'
with open(file_name, 'r') as f:
	n, k, m = list(map(int, f.readline().split()))
	nums = list(map(int, f.readlines()))

nums.sort()
cheapest_phones = nums[:k]
premium_phones = nums[-m:]
print(min(premium_phones), sum(cheapest_phones) // len(cheapest_phones))