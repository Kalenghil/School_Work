def smallest_divisor(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return i
    return 1


i = 699_999
len_ans = 0
while True:
    i += 1
    small = smallest_divisor(i)
    if small == 1:
        continue
    big = i // small
    if (big + small) % 10 == 8:
        len_ans += 1
        print(i, small + big)
    if len_ans >= 5:
        break
