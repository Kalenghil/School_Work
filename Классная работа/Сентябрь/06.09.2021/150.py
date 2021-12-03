with open(r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\17data\17-1.txt", "r") as f:
    nums = [int(i) for i in f.readlines()]
    ans = list()
    for i in range(len(nums) - 1):
        if (
            (nums[i] % 7 == 0 and nums[i + 1] % 17 != 0) or
            (nums[i + 1] % 7 == 0 and nums[i] % 17 != 0)
        ):
            ans.append((nums[i], nums[i + 1]))
    ans.sort(key=lambda x: x[0] + x[1])
    print(len(ans), sum(ans[0]))
    f.close()
