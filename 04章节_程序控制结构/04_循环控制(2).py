"""
多重循环控制(重难点)

- 说明
1、将一个循环放在另一个循环体内，就形成了嵌套循环。其中，for、while均可以作为外层循环和内层循环。【建议一般使用两层，最多不超过三层，否则，代码的可读性不好】
2、实质上，嵌套循环就是把内层循环当成外层循环的循环体。
3、如果外层循环次数为m次，内层循环为n次，则内层循环体实际上需要执行m*n次。
    count = 0
    for i in range(2):
        for j in range(3):
            count += 1
            print("ok")
    print(f"总共输出ok了{count}次")  # 总共输出ok了6次
"""
print("---" * 20)
content = "编写一个程序，可以接收一个整数，表示层数(total),打印出空心金字塔。"
"""
思路分析
- 先死后活
1、写死层数：不考虑层数变化，假定就是5层
2、将常量改为可接收的变量
- 化繁为简
1、打印矩形
2、打印直角三角形1
3、打印直角三角形2
4、打印实心金字塔
5、打印空心金字塔
"""
print(f"demo:{content}")

print("一、写死层数：不考虑层数变化，假定就是5层")
print("1、打印矩形")
# i控制层数
for i in range(1, 6):
    # j控制每层*的个数
    for j in range(1, 6):
        # end=""表示输出不换行
        print("*", end="")
    # 每层输出后换行
    print("")

print("2、打印直角三角形1")
# i控制层数
for i in range(1, 6):
    # j控制每层*的个数
    for j in range(i):
        # end=""表示输出不换行
        print("*", end="")
    # 每层输出后换行
    print("")

print("3、打印直角三角形2")
# i控制层数
for i in range(1, 6):
    # j控制每层*的个数
    for j in range(2 * i - 1):
        # end=""表示输出不换行
        print("*", end="")
    # 每层输出后换行
    print("")

print("4、打印实心金字塔")
# i控制层数
for i in range(1, 6):
    # k控制输出空格数
    for k in range(5 - i):
        print(" ", end="")
    # j控制每层*的个数
    for j in range(2 * i - 1):
        # end=""表示输出不换行
        print("*", end="")
    # 每层输出后换行
    print("")

print("5、打印空心金字塔")
# i控制层数
for i in range(1, 6):
    # k控制输出空格数
    for k in range(5 - i):
        print(" ", end="")
    # j控制每层*的个数
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2 or i == 5:
            # end=""表示输出不换行
            print("*", end="")
        else:
            print(" ", end="")
    # 每层输出后换行
    print("")

print("---" * 20)
print("二、将常量改为可接收的变量")
total = int(input("请输入层数："))
# i控制层数
for i in range(total):
    # k控制输出空格数
    for k in range(total - 1 - i):
        print(" ", end="")
    # j控制每层*的个数
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == total - 1:
            # end=""表示输出不换行
            print("*", end="")
        else:
            print(" ", end="")
    # 每层输出后换行
    print("")


