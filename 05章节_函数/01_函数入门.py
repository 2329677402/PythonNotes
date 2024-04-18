"""
- 函数说明
① 为完成某一功能的程序指令(语句)的集合，称为函数
② 在Python中，函数分为：系统函数、自定义函数
    - 内置函数: https://docs.python.org/zh-cn/3.11/library/functions.html
    - 模块提供的函数: https://docs.python.org/zh-cn/3.11/library/math.html

- 优势
① 提高代码的复用性
② 可以将实现的细节封装起来，提供给其他用户来调用

- 基本语法
# 使用def关键字定义函数
def max(a, b):
    # 函数体
    if a > b:
        return a
    else:
        return b
① 函数代码块以def关键字开头，后接函数标识符名称和圆括号()
② 函数内容以冒号:起始，并且缩进
③ 函数参数(a, b)，可以有多个，也可以没有即直接是()，(a, b)也称为形参列表
④ 函数可以有返回值，也可以没有，如果没有return相当于返回None

- 函数调用
max(10, 20)
① 函数定义完成后，并不会自动执行，需要主动调用，才会执行
② 调用方式：函数名(实参列表),比如max(10, 20)
"""
print("---" * 20)
content1 = "自定义cry函数，输出“小猫，喵喵喵...”"
print(f"demo1:{content1}")


def cry():
    print("小猫，喵喵喵...")


cry()  # 小猫，喵喵喵...

print("---" * 20)
content2 = "自定义cal01函数，可以计算从1+...+1000的结果"
print(f"demo2:{content2}")


def cal01(a, b):
    sum = 0
    for i in range(a, b + 1):
        sum += i
    print(sum)


cal01(1, 1000)  # 500500

print("---" * 20)
content3 = "自定义cal02函数，该函数可以接收一个数n，计算从1+...+n的结果"
print(f"demo3:{content3}")


def cal02():
    n = int(input("请输入整数："))
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(sum)


cal02()
# 请输入整数：5
# 15

print("---" * 20)
content4 = "自定义get_sum函数,可以计算两个数的和，并返回结果"
print(f"demo4:{content4}")


def get_sum(a, b):
    return a + b


res = get_sum(10, 50)
print(res)  # 60
