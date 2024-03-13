"""
养鸡场问题:
一个养鸡场有6只鸡，它们的体重分别是3kg，5kg,1kg，3.4kg,2kg，50kg。请问这六只鸡的总体重是多少?平均体重是多少？
"""

# 传统方法,定义6个变量接收体重
h1 = 3
h2 = 5
h3 = 1
h4 = 3.4
h5 = 2
h6 = 50
total_weight = h1 + h2 + h3 + h4 + h5 + h6
avg_weight = total_weight / 6

# Python内置函数round(number, ndigits=None):返回 number 舍入到小数点后 ndigits 位精度的值.如果 ndigits 被省略或为 None，则返回最接近输入值的整数
# https://docs.python.org/zh-cn/3.11/library/functions.html#round
print(round(25.567, 2))  # 25.57
print(f"总体重是:{total_weight},平均体重是:{round(avg_weight, 1)}")  # 总体重是:64.4,平均体重是:10.7

"""
数据容器
- 基本介绍
    1、数据容器是一种数据类型，有些地方也简称为容器/collections
    2、数据容器可以存放多个数据，每一个数据也被称为一个元素
    3、存放的数据/元素可以是任意类型
    4、简单的说，数据容器就是一种可以存放多个数据/元素的数据类型
- 分类
    1、列表(list)  https://docs.python.org/zh-cn/3.11/library/stdtypes.html#list
    2、元组(tuple) https://docs.python.org/zh-cn/3.11/library/stdtypes.html#tuple
    3、字符串(str) https://docs.python.org/zh-cn/3.11/library/stdtypes.html#str
    4、集合(set)   https://docs.python.org/zh-cn/3.11/library/stdtypes.html#set
    5、字典(dict)  https://docs.python.org/zh-cn/3.11/library/stdtypes.html#dict
"""