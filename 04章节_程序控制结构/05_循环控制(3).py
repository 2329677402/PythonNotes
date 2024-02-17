"""
多重循环练习题
"""

print("---" * 20)
content1 = "接收一个整数，表示层数(total),打印出空心菱形。"
print(f"demo1:{content1}")
# 写死层数，假设为9层
for i in range(1, 10):
    if i <= 5:
        for k in range(5 - i):
            print(" ", end="")
    if i > 5:
        for k in range(i - 5):
            print(" ", end="")
    if i <= 5:
        for j in range(2 * i - 1):
            if j == 0 or j == 2 * i - 2:
                print("*", end="")
            else:
                print(" ", end="")
        print("")
    if i > 5:
        i = i - 2 * (i - 5)
        for j in range(2 * i - 1):
            if j == 0 or j == 2 * i - 2:
                print("*", end="")
            else:
                print(" ", end="")
        print("")

# 接收变量
total = int(input("请输入层数："))
for i in range(total):
    if i <= total // 2:
        for k in range(total // 2 - i):
            print(" ", end="")
    if i > total // 2:
        for k in range(i - total // 2):
            print(" ", end="")
    if i <= total // 2:
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:
                print("*", end="")
            else:
                print(" ", end="")
        print("")
    if i > total // 2:
        i = i - 2 * (i - total // 2)
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:
                print("*", end="")
            else:
                print(" ", end="")
        print("")

print("---" * 20)
content2 = "接收一个整数，表示层数(total),打印出空心菱形，使用while实现。"
print(f"demo2:{content2}")
# 写死层数，假设为9层
print("1、打印矩形")
i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print("*", end="")
        j += 1
    print("")
    i += 1

print("2、打印三角形")
i = 1
while i <= 9:
    j = 1
    if i <= 5:
        while j <= 2 * i - 1:
            print("*", end="")
            j += 1
    else:
        while j <= 2 * (9 - i) + 1:
            print("*", end="")
            j += 1
    print("")
    i += 1

print("3、打印菱形")
i = 1
while i <= 9:
    k = 1
    if i <= 5:
        while k <= 5 - i:
            print(" ", end="")
            k += 1
    else:
        while k <= i - 5:
            print(" ", end="")
            k += 1
    j = 1
    if i <= 5:
        while j <= 2 * i - 1:
            print("*", end="")
            j += 1
    else:
        while j <= 2 * (9 - i) + 1:
            print("*", end="")
            j += 1
    print("")
    i += 1

print("4、打印空心菱形")
i = 1
while i <= 9:
    k = 1
    if i <= 5:
        while k <= 5 - i:
            print(" ", end="")
            k += 1
    else:
        while k <= i - 5:
            print(" ", end="")
            k += 1
    j = 1
    if i <= 5:
        star_count = 2 * i - 1
    else:
        star_count = 2 * (9 - i) + 1
    while j <= star_count:
        if j == 1 or j == star_count:
            print("*", end="")
        else:
            print(" ", end="")
        j += 1
    print("")
    i += 1

print("5、接收变量")
total = int(input("请输入层数："))
# 获取中间层
mid = (total + 1) // 2
# 初始化变量i的层数，用于控制层数
i = 1
while i <= total:
    # 初始化变量k的空格数，用于控制每行第一个*前的空格数量
    k = 1
    if i <= mid:
        while k <= mid - i:
            print(" ", end="")
            k += 1
    else:
        while k <= i - mid:
            print(" ", end="")
            k += 1
    # 初始化变量j的*数量，用于控制每行的*数量
    j = 1
    if i <= mid:
        star_count = 2 * i - 1
    else:
        star_count = 2 * (total - i) + 1
    while j <= star_count:
        if j == 1 or j == star_count:
            print("*", end="")
        else:
            print(" ", end="")
        j += 1
    print("")
    i += 1
