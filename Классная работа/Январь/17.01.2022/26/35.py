file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\26data\26-j7.txt'
with open(file_name, 'r') as f:
	amount = int(f.readline())
	participants = list(map(int, f.readlines()))

participants.sort(reverse=True)
total_sum = sum(participants)
rich_sum = sum(participants[:int(amount * 0.2)])
poor_sum = total_sum - rich_sum
print(rich_sum, poor_sum)
