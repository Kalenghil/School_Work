from pprint import pprint


num = 609
nums = [0] * 9
print(nums)
for i in range(2, 11):
    temp = num
    s = str()
    while temp:
        s = str(temp % i) + s
        temp //= i
    print(i - 2)
    nums[i - 2] = (i, s[0] + s[-1])
pprint([i for i in nums])
