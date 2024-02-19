"""
斐波那契数列、猴子吃桃问题、汉诺塔问题
"""
print("---" * 20)
content1 = "请使用递归的方式求出斐波那契数1,1,2,3,5,8,13...给你一个整数n，求出它的值是多少？(即：第n个位置对应的斐波那契数)"
print(f"demo1:{content1}")


def demo1(n):
    """
    功能：返回第 n个位置对应的斐波那契数
    :param n: 接收一个整数n,n>=1
    :return: 返回斐波那契数
    """
    if n == 1 or n == 2:
        return 1
    # 如果n > 2,则n对应的斐波那契数为n - 1和n - 2对应的斐波那契数之和
    else:
        return demo1(n - 1) + demo1(n - 2)


print(demo1(7))  # 13

print("---" * 20)
content2 = ("猴子吃桃子问题：有一堆桃子，猴子第一天吃了其中的一半，并再多吃了一个！"
            "以后每天猴子都吃其中的一半，然后再多吃一个。当到第10天时，想再吃时（即还没吃），发现只有1个桃子了。"
            "问题：最初共多少个桃子?")
print(f"demo2:{content2}")

"""
- 思路分析
- day代表天数, peach代表当天开始时的桃子数量
1. day == 10, peach10 == 1
2. day == 9,  peach9 - (peach9 / 2 + 1) = peach10, peach9 == 4
3. day == 8,  peach8 - (peach8 / 2 + 1) = peach9, peach8 == 10
...
10.day == 1, peach1 - (peach1 / 2 + 1) = peach2, peach1 == ???
由此推导出公式:
第n天最开始时的桃子数量为：peach(n) = (peach(n + 1) + 1) * 2
"""


def demo2(n):
    """
    功能：求出最初有多少个桃子
    :param n: 天数
    :return: 剩余桃子数
    """
    if n == 10:
        return 1
    else:
        return (demo2(n + 1) + 1) * 2


print("第一天的桃子数量为:", demo2(1))  # 1534

print("---" * 20)
content3 = "求函数值，已知f(1)=3;f(n)=2*f(n-1)+1;请使用递归的思想编程，求出f(n)的值?"
print(f"demo3:{content3}")


def demo3(n):
    if n == 1:
        return 3
    else:
        return demo3(n - 1) * 2 + 1


print(demo3(3))  # 15

# 应用实例-汉诺塔问题
print("---" * 20)
content4 = """
汉诺塔：汉诺塔（又称河内塔）问题是源于印度一个古老传说的益智玩具。大梵天创造世界的时候做了三根金刚石柱子，
在一根柱子上从下往上按照大小顺序摞着64片圆盘。大梵天命令婆罗门把圆盘从下面开始按大小顺序重新摆放在另一根柱子上。
并且规定，在小圆盘上不能放大圆盘，在三根柱子之间一次只能移动一个圆盘。
"""
print(f"demo4:{content4}")


def hanoi_tower(num, a, b, c):
    """
    功能：输出num个轮盘移动的顺序
    :param num: 轮盘数量
    :param a: A柱子
    :param b: B柱子
    :param c: C柱子
    :return:
    """
    # 一个轮盘的情况
    if num == 1:
        print(f"第1个轮盘从:{a}柱->{c}柱")
    # 多个轮盘的情况
    else:
        # 有多个轮盘则将它看为两部分:① 最下面的大轮盘 ② 大轮盘之上的所有轮盘
        # 移动② 轮盘到B柱,这个过程会借助到C柱
        hanoi_tower(num - 1, a, c, b)
        # 移动① 轮盘到C柱
        print(f"第{num}个轮盘从:{a}柱->{c}柱")
        # 把② 轮盘从B柱移动到C柱,这个过程会借助到A柱
        hanoi_tower(num - 1, b, a, c)


hanoi_tower(5, "A", "B", "C")
