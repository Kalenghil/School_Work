import math
import time
from functools import lru_cache


@lru_cache(None)
def check(num):
    return True


file_name = r'C:\Users\Bosnian\Documents\GitHub\School_Work\Материалы\27data\75\27-75b.txt'
max_sum = -math.inf

start = time.time()
summ = 0
counter = 0
cur_len = 0

with open(file_name, 'r') as f:
    amount = int(f.readline())
    k = 43
    tails = [[math.inf, math.inf] for _ in range(k)]

    for _ in range(amount):
        num = int(f.readline())
        cur_len += 1
        summ += num
        if check(num):
            counter += 1

        rem = summ % k
        if rem == 0 and max_sum < summ:
            max_sum = summ
            ans = cur_len

        if tails[rem] != math.inf and summ - tails[rem][0] > max_sum:
            max_sum = summ - tails[rem][0]
            ans = cur_len - tails[rem][1]

        if tails[rem][0] > summ:
            tails[rem][0] = summ
            tails[rem][1] = cur_len
print(max_sum, ans, f'{time.time() - start:.4f}')