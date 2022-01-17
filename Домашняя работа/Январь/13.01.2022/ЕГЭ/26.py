file_name = r'D:\WORK\11 класс\Макиевский Кирилл\Материалы\Варианты\Вариант 102-2022с\26.txt'
things = list()
with open(file_name, 'r') as f:
	amount, max_sum = list(map(int, f.readline().split()))
	for _ in range(amount):
		raw_string = f.readline().strip().split()
		price, idx = int(raw_string[0]), raw_string[1]
		things.append((price, idx))

things_to_buy = list()
our_sum = 0
things.sort(key=lambda x: x[0])
for i in range(len(things)):
	if our_sum + things[i][0] <= max_sum:
		things_to_buy.append(things[i])
		our_sum += things[i][0]
	else:
		exit_idx = i
		break
print(max_sum - our_sum)
for i in range(len(things_to_buy) - 1, -1, -1):
	if things_to_buy[i][1] == 'A':
		for j in range(exit_idx, len(things)):
			if things[j][1] == 'B':
				if our_sum - things_to_buy[i][0] + things[j][0] <= max_sum:
					things_to_buy[i], things[j] = things[j], things_to_buy[i]
					our_sum += things_to_buy[i][0] - things[j][0]
					exit_idx = j
					print(f'{things[j]} => {things_to_buy[i]}, {max_sum - our_sum}')
					break
print(len(things_to_buy), sum(list(zip(*things_to_buy))[0]), our_sum)
print(len(list(filter(lambda x: x[1] == 'B', things_to_buy))), max_sum - our_sum)
print(things_to_buy[:])
print(things[len(things_to_buy):])