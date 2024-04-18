"""
- 基本语法
def 函数名(参数列表):
    语句...
    return 返回值

- 说明
如果没有return语句,默认返回None,None是内置常量,通常用来代表空值的对象
参考:https://docs.python.org/zh-cn/3.11/library/constants.html
"""


def f1():
    print("hi")


r = f1()  # hi
# 函数中没有return语句,就返回None
print("r :", r)  # r : None
print("r(id) :", id(r))  # r(id) : 140732879171264
