with open(r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\17data\17-2.txt", "r") as f:
    # nums = [int(i) for i in f.readlines()]
    nums = list(map(int, f.readlines()))
    min_num = min(nums)
    print(nums.count(min_num),
          len(nums) - nums[::-1].index(min_num))
