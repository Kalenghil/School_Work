with open(r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\17data\17-1.txt", "r") as f:
    nums = [int(i) for i in f.readlines()]
    ans = list()
    for i in range(len(nums) - 1):
        if (
            (nums[i] % 3 == 0 and abs(nums[i]) % 10 == 6) or
            (nums[i + 1] % 3 == 0 and abs(nums[i + 1]) % 10 == 6)
        ):
            ans.append((nums[i], nums[i + 1], min(nums[i], nums[i + 1])))
    ans.sort(key=lambda x: x[2])
    print(len(ans), ans[0][2])
    f.close()
