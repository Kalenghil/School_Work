with open(r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\17data\17-1.txt", "r") as f:
    nums = [int(i) for i in f.readlines()]
    ans = list()
    for i in range(len(nums) - 1):
        if (
            (nums[i] % 9 == 0 and nums[i + 1] % 9 != 0 and f'{nums[i + 1]:o}'[-1] == '3') or
            (nums[i + 1] % 9 == 0 and nums[i] % 9 != 0 and f'{nums[i]:o}'[-1] == '3')
        ):
            ans.append((nums[i], nums[i + 1], max(nums[i], nums[i + 1])))
    ans.sort(key=lambda x: x[2], reverse=True)
    print(len(ans), ans[0][2])
    f.close()
