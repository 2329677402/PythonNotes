# 基本数据类型
# 定义变量
import sys

name = "jocker"  # 字符串
age = 18  # 整型
score = 90.0  # 浮点型
gender = "男"  # 字符串
is_pass = True  # 布尔类型
# type()函数用于查看数据的类型
print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>
print(type(score))  # <class 'float'>
print(type(gender))  # <class 'str'>
print(type(is_pass))  # <class 'bool'>

print("---" * 20)
print("1、整数类型")
# 1、整数类型
# 1、Python中的整型，可以表示很大的数(官方最大值：the limit (4300) for integer)
# print(9**8888) # ValueError

# 2、Python的整数有十进制，十六进制，八进制，二进制
# -十进制就是我们最常见的写法，比如1、66、123等
print(10)  # 10
# -十六进制写法：加前缀0x，由0-9和A-F的数字和字母组合
print(0x10)  # 16
# -八进制写法：加前缀0o，由0-7数字组合
print(0o10)  # 8
# -二进制写法：加前缀0b，只有0和1数字组合
print(0b10)  # 2
# -运行时，会自动转换为十进制输出

# 3、Python中的整型占多少个字节
# 字节(byte)：计算机中基本存储单元
# 位(bit)：计算机中的最小存储单位
# 1byte = 8 bit
# 1)字节数随着数字增大而增大（即：python整型是变长的）
# 2)每次的增量是4个字节
n1 = 0
n2 = 1
n3 = 2
n4 = 2 ** 15
n5 = 2 ** 30
n6 = 2 ** 128
# 在Python中，可以通过sys.getsizeof返回对象的大小(按字节单位返回)
print(n1, sys.getsizeof(n1), '类型', type(n1))  # 0 24 类型 <class 'int'>
print(n2, sys.getsizeof(n2), '类型', type(n2))  # 1 28 类型 <class 'int'>
print(n3, sys.getsizeof(n3), '类型', type(n3))  # 2 28 类型 <class 'int'>
print(n4, sys.getsizeof(n4), '类型', type(n4))  # 32768 28 类型 <class 'int'>
print(n5, sys.getsizeof(n5), '类型', type(n5))  # 1073741824 32 类型 <class 'int'>
print(n6, sys.getsizeof(n6), '类型', type(n6))  # 340282366920938463463374607431768211456 44 类型 <class 'int'>

print("---" * 20)
print("2、浮点类型")
# 2、浮点类型
# 1、浮点数表示形式如下
# -十进制数形式：如：5.12 .512（必须有小数点）
n1 = .512
print(n1)  # 0.512
# -科学计数法形式：如：5.12e2,5.12E-2
n2 = 4.5e2
n3 = 4.50E-2
print(n2, n3)  # 450.0 0.045

# 2、浮点数有大小限制边界值为：
# max=1.7976931348623157e+308
# min=2.2250738585072014e-308
print(
    sys.float_info)  # sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

# 3、浮点类型数据计算后，存在精度损失，可以用Decimal类进行精确计算
n1 = 8.1 / 3
print(n1)  # 2.6999999999999997
# 解决方法：导入Decimal类
from decimal import Decimal

n2 = Decimal("8.1") / Decimal("3")
print(n2)

print("---" * 20)
print("3、布尔类型")
# 3、布尔类型
# 1、布尔类型也叫bool类型，取值True和False
# 2、Tue和 False都是关键字，表示布尔值
# 3、bool类型适于逻辑运算，一般用于程序流程控制
# -条件控制语句
# -循环控制语句
# 比如判断某个条件是否成立，或者在某个条件满足时执行某些代码
n1 = 100
n2 = 200
result = n1 > n2
print(result, type(result))  # False <class 'bool'>
# 1、布尔类型只有两个值：True和False
# 2、布尔类型可以和其他数据类型进行比较，比如数字、字符串等。在比较时，Python会将True视为1，False 视为0
n1 = False
n2 = True
print(n1 + 10)  # 10
print(n2 + 10)  # 11
if n1 == 0:
    print("等于")  # 等于
if n2 == 1:
    print("等于")  # 等于
# 3、在Python中，非0被视为真值，0值被视为假值
if 0:
    print("hhh")  # 不输出
if -1:
    print("xxx")  # xxx
if "哈哈":
    print("haha")  # haha

print("---" * 20)
print("4、字符串类型")
# 4、字符串类型
# 1、Python 不支持单字符类型，单字符在Python 中也是作为一个字符串使用
# 2、用三个单引号'''内容''',或三个双引号"""内容"""可以使字符串内容保持原样输出，在输出格式复杂的内容是比较有用的，比如输出一段代码。
content = '''def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True'''
print(content)
# 3、在字符串前面加'r'可以使整个字符串不会被转义
n1 = "tom\nsimom\tjack"
print(n1)
# tom
# simom	jack
n2 = r"tom\nsimom\tjack"
print(n2)
# tom\nsimom\tjack
