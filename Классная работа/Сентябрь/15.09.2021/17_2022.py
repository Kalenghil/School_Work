with open(r"D:\МАТЕРИАЛЫ\ЕГЭ\КЕГЭ_демо 2022_проект\Доп. файлы\Задание 17\17.txt", "r") as f:
    nums = list(map(int, f.readlines()))
    ans = list()
    for i in range(len(nums) - 1):
        if (abs(nums[i] ) % 3 == 0) or (abs(nums[i + 1]) % 3 == 0):
            ans.append(nums[i] + nums[i + 1])
    print(len(ans), max(ans))
    f.close()
