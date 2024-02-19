"""
问题分析
1.f1和f2都有对两个数求最大值的需求
2.如果有更多的函数也有对两个数求最大的需求，在每个函数都写一份相同代码会冗余，而且，不利用维护
3.解决方案，编写一个函数(该函数可以返回两个数的最大值），
4.将该函数作为参数传给f1,f2->即：将函数作为参数传递
"""


# 未将函数作为参数传递
def f1(n1, n2):
    max_val = n1 if n1 > n2 else n2
    return max_val


def f2(n1, n2):
    max_val = n1 if n1 > n2 else n2
    return n1 + n2, max_val


# 将函数作为参数传递
def get_max_val(n1, n2):
    max_val = n1 if n1 > n2 else n2
    return max_val


def f3(fun, n1, n2):
    """
    功能：调用fun返回n1和n2的最大值
    :param fun:表示接收一个函数
    :param n1:传入数值
    :param n2:传入数值
    :return:最大值
    """
    return fun(n1, n2)


def f4(fun, n1, n2):
    """
    功能：调用fun返回n1和n2的最大值,同时返回两个数的和
    :param fun:
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2, fun(n1, n2)


print(f3(get_max_val, 10, 20))  # 20
x, y = f4(get_max_val, 10, -20)
print(f"x = {x}, y = {y}")  # x = -10, y = 10


# 注意事项和细节
# 1、函数作为参数传递，传递的不是数据，而是业务处理逻辑
# 2、一个函数，可以接收多个函数作为参数传入
def sum(n1, n2):
    return n1 + n2


def f5(fun, fun2, n1, n2):
    return fun(n1, n2), fun2(n1, n2)


print(f5(get_max_val, sum, 50, 60))  # (60, 110)
