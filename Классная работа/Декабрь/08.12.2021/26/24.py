def mean(nums):
	return sum(nums) // len(nums)


file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\26data\26-k4.txt'
with open(file_name, 'r') as f:
	n, k = list(map(int, f.readline().split()))
	nums = list(map(int, f.readlines()))

nums.sort(reverse=True)
good_marks = nums[:k]
worse_marks = nums[k:2 * k]
print(mean(good_marks), mean(worse_marks))
