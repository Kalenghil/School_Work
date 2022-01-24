file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\26data\26-j9.txt'
# file_name = r'38_test.txt'
with open(file_name, 'r') as f:
	max_sum, amount = list(map(int, f.readline().split()))
	files = list(map(int, f.readlines()))

print(max_sum, amount)
files.sort(reverse=True)
print(files)
our_sum = 0
ans = list()
left, right = 0, -1
flag = True
while True:
	while our_sum + files[left] > max_sum:
		left += 1
		if left >= len(files) - right:
			flag = False
			break
	if flag is False:
		break
	our_sum += files[left]
	ans.append(files[left])
	left += 1
	if our_sum + files[right] > max_sum:
		break
	else:
		our_sum += files[right]
		ans.append(files[right])
		right -= 1

print(ans)
print(max_sum, our_sum, sum(ans))
print(amount, len(ans))
print(f'Answer is: {len(ans)} {ans[-1]}')
