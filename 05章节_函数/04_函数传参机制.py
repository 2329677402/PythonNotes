"""
    字符串和数值类型传参机制
"""


# 数值类型
def f1(a):
    print(f"f1() a的值：{a} 地址:{id(a)}")
    a += 1
    print(f"f1() a的值：{a} 地址:{id(a)}")


a = 10
print(f"调用f1()前 a的值:{a} 地址:{id(a)}")
f1(a)
print(f"调用f1()后 a的值:{a} 地址:{id(a)}")

"""
运行结果：
调用f1()前 a的值:10 地址:1536901317136
f1() a的值：10 地址:1536901317136
f1() a的值：11 地址:1536901317168
调用f1()后 a的值:10 地址:1536901317136
"""

print("---" * 20)


# 字符串类型
def f2(name):
    print(f"f2() name的值：{name} 地址:{id(name)}")
    name += " Hi"
    print(f"f2() name的值：{name} 地址:{id(name)}")


name = "Simon"
print(f"调用f2()前 name的值:{name} 地址:{id(name)}")
f2(name)
print(f"调用f2()后 name的值:{name} 地址:{id(name)}")

"""
运行结果：
调用f2()前 name的值:Simon 地址:2540021950640
f2() name的值：Simon 地址:2540021950640
f2() name的值：Simon Hi 地址:2540022270832
调用f2()后 name的值:Simon 地址:2540021950640
"""

# 由此可见：在外部定义的数值类型或字符串类型,不会被函数内部的语句所影响
