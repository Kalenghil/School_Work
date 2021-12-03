from pprint import pprint
from math import inf

diffs = [inf] * 7
big, sml = 0, 0
filepath = r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\27data\46\27-46b.txt"
with open(filepath, 'r') as f:
    amount = int(f.readline())
    for _ in range(amount):
        a, b = sorted(list(map(int, f.readline().split())))
        diffs[(b - a) % 7] = min(diffs[(b - a) % 7], (b - a))
        big += b
        sml += a

print(f'{big}: {big % 7}; {sml}: {sml % 7}')
print(*list(enumerate(diffs)))


rem_diff = ((big % 7) - (sml % 7))
if rem_diff == 0:
    print(big)
else:
    if rem_diff < 0:
        rem_diff = 7 - abs(rem_diff)
    new_big = big - diffs[rem_diff]
    print(f'answer: {new_big}, diff: {diffs[rem_diff]}')

# b : 410884352 410884352
# a : 115110 109307
