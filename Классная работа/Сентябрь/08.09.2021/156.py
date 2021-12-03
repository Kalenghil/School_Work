with open(r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\17data\17-2.txt", "r") as f:
    nums = [int(i) for i in f.readlines()]
    ans = list()
    max_num = max(nums)
    print(nums.count(max_num), nums.index(max_num) + 1)
    f.close()
