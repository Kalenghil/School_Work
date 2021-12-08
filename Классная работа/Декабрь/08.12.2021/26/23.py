file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\26data\26-k3.txt'
with open(file_name, 'r') as f:
	n, k, m = list(map(int, f.readline().split()))
	nums = list(map(int, f.readlines()))

nums.sort(reverse=True)
winner = nums[k - 1]
prizer = nums[m + k - 1]
print(winner, prizer)
