# Python根据该变量使用的上下文在运行时决定的

# 1、隐式类型转换
print("---" * 20)
print("1、隐式类型转换")
var1 = 10
print("var1的类型：", type(var1))  # var1的类型： <class 'int'>
var2 = 1.1
print("var2的类型：", type(var2))  # var2的类型： <class 'float'>
var3 = var1 + var2
print("var3 = ", var3, "var3的类型：", type(var3))  # var3 =  11.1 var3的类型： <class 'float'>

# 2、显式类型转换
print("---" * 20)
print("2、显式类型转换")
n1 = 10
print("n1的类型：", type(n1))  # n1的类型： <class 'int'>
n2 = float(n1)
print("n2的类型：", type(n2))  # n2的类型： <class 'float'>
n3 = str(n1)
print("n3的类型：", type(n3))  # n3的类型： <class 'str'>

# 3、显式类型转换注意事项
print("---" * 20)
print("3、显式类型转换注意事项")
a = 100
b = 10.01
# demo1:不管什么值的int,float都可以转成str,str(x)将对象 x 转换为字符串
print("---" * 20)
print("demo1")
print(a, type(a), str(a), type(str(a)))  # 100 <class 'int'> 100 <class 'str'>
print(b, type(b), str(b), type(str(b)))  # 10.01 <class 'float'> 10.01 <class 'str'>

# demo2:int转成float时,会增加小数部分,float转成int时,会去掉小数部分
print("---" * 20)
print("demo2")
print(a, float(a))  # 100 100.0
print(b, int(b))  # 10.01 10

# demo3:str转int,float使用int(x),float(x)将对象 x 转换为int/float
print("---" * 20)
print("demo3")
x = "12.3"
print(x, type(x), float(x), type(float(x)))  # 12.3 <class 'str'> 12.3 <class 'float'>
y = "123"
print(y, type(y), int(y), type(int(y)))  # 123 <class 'str'> 123 <class 'int'>

# demo4:在将str类型转为基本数据类型时，要确保str值能够转为有效数据，如果格式不正确，程序会报ValueError
print("---" * 20)
print("demo4")
n4 = "12.3"
print(float(n4))  # 12.3
# print(int(n4)) # ValueError
n5 = "hello"
# print(float(n5)) # ValueError
# print(int(n5)) # ValueError

# demo5:对一个变量进行强制转换后，会返回一个数据/值，但是并不会改变原变量的数据/值
print("---" * 20)
print("demo5")
n6 = 10
n7 = float(n6)
print(n6, type(n6))  # 10 <class 'int'>
print(n7, type(n7), type(n6))  # 10.0 <class 'float'> <class 'int'>

# 练习题
print("---" * 20)
print("练习题")
i = 10
j = float(i)  # 10.0
print(type(i))  # int
print(type(j))  # float

i = j + 1  # 11.0
print(type(i))  # float
print(type(j))  # float

print(i)  # 11.0
print(int(i))  # 11
print(type(i))  # float
