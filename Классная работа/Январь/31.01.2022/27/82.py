import math
import time
from functools import lru_cache


@lru_cache(None)
def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


file_name = r'C:\Users\Bosnian\Documents\GitHub\School_Work\Материалы\27data\82\27-82b.txt'
max_sum = -math.inf

start = time.time()
summ = 0
counter = 0
with open(file_name, 'r') as f:
    amount = int(f.readline())
    k = 9
    tails = [math.inf] * k

    for _ in range(amount):
        num = int(f.readline())
        summ += num
        if is_prime(num):
            counter += 1

        rem = counter % k
        if rem == 0:
            max_sum = max(max_sum, summ)

        if tails[rem] != math.inf:
            max_sum = max(summ - tails[rem], max_sum)

        tails[rem] = min(tails[rem], summ)

print(max_sum, f'{time.time() - start:.4f}')
