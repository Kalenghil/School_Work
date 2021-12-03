from pprint import pprint
import math

file_path = r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\27data\57\27-57b.txt"
with open(file_path, 'r') as f:
    amount = int(f.readline())
    nums = sorted(list(map(int, f.readlines())), reverse=False)
    dived_nums = [[].copy() for _ in range(9)]
    for num in nums:
        dived_nums[num % 9].append(num)

pprint([(num, num % 9) for num in nums[:20]])
summ = 0
for _ in range(2):
    pairs = [0] * 5
    for i in range(5):
        if i == 0:
            pairs[i] = dived_nums[0][0] + dived_nums[0][1]
        else:
            pairs[i] = dived_nums[i][0] + dived_nums[9 - i][0]
    max_pair = min(pairs)
    print(pairs)
    summ += max_pair
    if max_pair == pairs[0]:
        dived_nums[0].pop(0)
        dived_nums[0].pop(0)
    for i in range(1, 5):
        if max_pair == pairs[i]:
            dived_nums[i].pop(0)
            dived_nums[9 - i].pop(0)
            break
print(summ)
