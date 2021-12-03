with open(r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\17data\17-1.txt", "r") as f:
    nums = [int(i) for i in f.readlines()]
    ans = list()
    for i in range(1, len(nums) - 1):
        if (nums[i] > nums[i - 1] and nums[i] > nums[i + 1]):
            ans.append((nums[i], i))
    ans.sort(key=lambda x: x[1])
    print(len(ans), min([abs(ans[i][1] - ans[i + 1][1])
                         for i in range(len(ans) - 1)]))
    f.close()
