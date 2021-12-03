with open(r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\17data\17-1.txt", "r") as f:
    nums = [int(i) for i in f.readlines()]
    ans = list()
    for i in range(1, len(nums) - 1):
        if (nums[i] < nums[i - 1] and nums[i] < nums[i + 1]):
            ans.append(nums[i])
    print(len(ans), max(ans))
    f.close()
