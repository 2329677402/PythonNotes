"""
- 基本介绍
    如果我们有这样一个需求，需要将函数作为参数进行传递，但是这个函数只使用一次，这时，我们可以考虑使用lambda匿名函数
    1、函数的定义
        -def关键字，可以定义带有名称的函数，可以重复使用
        -lambda关键字，可以定义匿名函数(无名称)，匿名函数只能使用一次
        -匿名函数用于临时创建一个函数，只使用一次的场景
    2、匿名函数基本语法
        -lambda 形参列表：函数体(一行代码)
        -lambda关键字，表示定义匿名函数
        -形参列表：比如num1，num2表示接收两个参数
"""

print("---" * 20)
content = "编写一个函数，可以接收一个匿名函数和两个数，通过匿名函数计算，返回两个数的最大值"
print(f"demo:{content}")


def f1(fun, n1, n2):
    print(f"fun类型:{type(fun)}")
    return fun(n1, n2)


"""
    1、lambda a, b: a if a > b else b 就是匿名函数
    2、不需要return, 运算结果就是返回值
"""
max_val = f1(lambda a, b: a if a > b else b, 20, 10)
print("max_val =", max_val)
