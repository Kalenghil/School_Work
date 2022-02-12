import time

start = time.time()
file_name = r'C:\Users\Bosnian\Documents\GitHub\School_Work\Материалы\27data\72\27-72b.txt'
summ = 0
k = 71
rems = [0] * k
ans = 0
with open(file_name, 'r') as f:
    amount = int(f.readline())
    for _ in range(amount):
        num = int(f.readline())
        summ += num

        rem = summ % k
        ans += rems[rem]
        if rem == 0:
            ans += 1

        rems[rem] += 1
        
print(ans, f'{time.time() - start:.4f}')
