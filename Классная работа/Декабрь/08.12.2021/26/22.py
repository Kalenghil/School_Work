file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\26data\26-k2.txt'
with open(file_name, 'r') as f:
	n, k = list(map(int, f.readline().split()))
	nums = sorted(list(map(int, f.readlines())))

nums = nums[k: -k]
max_num = max(nums)
mean = sum(nums) // len(nums)
print(max_num, mean)
