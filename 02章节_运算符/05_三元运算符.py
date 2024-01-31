"""
Python是一种极简主义的编程语言，它没有引入?：这个运算符，而是使用if else关键字来实现相同的功能
语法是：max = a if a > b else b
1、如果 a > b成立，就把a作为整个表达式的值，并赋给变量max
2、如果 a > b不成立，就把b作为整个表达式的值，并赋给变量max
"""
# demo1：取二者中的最大值
a = 10
b = 80
max = a if a > b else b
print(f"max = {max}")  # 80

# demo2:取三者中的最大值
a = 20
b = 50
c = 40
max = (a if a > b else b) if (a if a > b else b) > c else c
print(f"max = {max}")  # 50
