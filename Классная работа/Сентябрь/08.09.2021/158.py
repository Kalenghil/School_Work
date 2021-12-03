with open(r"D:\МАТЕРИАЛЫ\ЕГЭ\ege2022kp_сентябрь\17data\17-1.txt", "r") as f:
    nums = [int(i) for i in f.readlines()]
    ans = list()
    counter = 0
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            counter += 1
        else:
            ans.append(counter)
            counter = 0
    max_counter = max(ans)
    print(max_counter, len(list(filter(lambda x: x == max_counter, ans))))
    f.close()
