with open(r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\17data\17-1.txt", "r") as f:
    nums = [int(i) for i in f.readlines()]
    ans = list()
    for i in range(len(nums) - 1):
        if (nums[i] < nums[i + 1]):
            ans.append((nums[i], nums[i + 1], abs(nums[i] - nums[i + 1])))
    ans.sort(key=lambda x: x[2])
    print(len(ans), ans[0][2])
    f.close()
