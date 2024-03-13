[toc]



# :abc: 变量



## 一、格式化输出

> 基本介绍

- %操作符
- format()函数
- `f-strings`

> 代码演示

```py
# 定义变量
name = "jocker"
age = 18
score = 90.0
gender = "男"

# 1、%操作符
print("---" * 20)
print("个人信息：%s %d %s %.2f" % (name, age, gender, score))

# 2、format()函数
print("---" * 20)
print("个人信息：{} {} {} {}".format(name, age, score, gender))

# 3、f-strings
print("---" * 20)
print(f"个人信息：{name} {age} {score} {gender}")
```



## 二、加号的使用

> 代码演示

```py
# 定义变量
name = "jack"
score = 90.0

# 1、当左右两边都是数值型时，则做加法运算
print(score + 90)  # 180.0

# 2、当左右两边都是字符串，则做拼接运算
print(name + " hi ")  # jack hi
print("100" + "10")  # 10010
```



## 三、数据类型

> 基本数据类型

- [整数类型(int)](# 3.1 整数类型(int))
- [浮点类型(float)](# 3.2 浮点类型(float))
- [布尔类型(bool)](# 3.3 布尔类型(bool))
- [字符串类型(str)](# 3.4 字符串类型(str))

> 代码演示

```py
# 定义变量
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
```



### 3.1 整数类型(int)

> 整数类型介绍

1. Python中的整型，可以表示很大的数(官方最大值：the limit (4300) for integer).

```py
print(9**8888) # ValueError
```

2. Python的整数有十进制，十六进制，八进制，二进制.

```py
# -十进制就是我们最常见的写法，比如1、66、123等
print(10)  # 10

# -十六进制写法：加前缀0x，由0-9和A-F的数字和字母组合
print(0x10)  # 16

# -八进制写法：加前缀0o，由0-7数字组合
print(0o10)  # 8

# -二进制写法：加前缀0b，只有0和1数字组合
print(0b10)  # 2

# 运行时，会自动转换为十进制输出
```

3. Python中的整型占多少个字节.

```py
import sys

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
```



### 3.2 浮点类型(float)

> 浮点类型介绍

1. 浮点数表示形式如下.

```py
# -十进制数形式：如：5.12 .512（必须有小数点）
n1 = .512
print(n1)  # 0.512

# -科学计数法形式：如：5.12e2,5.12E-2
n2 = 4.5e2
n3 = 4.50E-2
print(n2, n3)  # 450.0 0.045
```

2. 浮点数有大小限制边界值.

```py
# max=1.7976931348623157e+308
# min=2.2250738585072014e-308

print(
    sys.float_info)  # sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
```

3. 浮点类型数据计算后，存在精度损失，可以用Decimal类进行精确计算.

```py
n1 = 8.1 / 3
print(n1)  # 2.6999999999999997

# 解决方法：导入Decimal类
from decimal import Decimal

n2 = Decimal("8.1") / Decimal("3")
print(n2)  # 2.7
```



### 3.3 布尔类型(bool)

> 布尔类型介绍

1. 布尔类型只有两个值：True和False.
2. Tue和False都是关键字，表示布尔值.
3. bool类型适于逻辑运算，一般用于程序流程控制.

```py
# 比如判断某个条件是否成立，或者在某个条件满足时执行某些代码.
n1 = 100
n2 = 200
result = n1 > n2
print(result, type(result))  # False <class 'bool'>
```

4. 布尔类型可以和其他数据类型进行比较，比如数字、字符串等.

```py
# 在比较时，Python会将True视为1，False视为0.
n1 = False
n2 = True
print(n1 + 10)  # 10
print(n2 + 10)  # 11
if n1 == 0:
    print("等于")  # 等于
if n2 == 1:
    print("等于")  # 等于
    
# 在Python中，非0被视为真值，0值被视为假值.
if 0:
    print("hhh")  # 不输出
if -1:
    print("xxx")  # xxx
if "哈哈":
    print("haha")  # haha
```



### 3.4 字符串类型(str)

> 字符串类型介绍

1. Python不支持单字符类型，单字符在Python中也是作为一个字符串使用.
2. 用三个单引号'''内容''',或三个双引号"""内容"""可以使字符串内容保持原样输出，在输出格式复杂的内容是比较有用的，比如输出一段代码.

```py
content = '''
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
'''
print(content)
```

3. 在字符串前面加'r'可以使整个字符串不会被转义.

```py
n1 = "tom\nsimom\tjack"
print(n1)
# tom
# simom	jack

n2 = r"tom\nsimom\tjack"
print(n2)
# tom\nsimom\tjack
```



## 四、字符串驻留机制

> 字符串驻留机制的好处

- 当需要值相同的字符串时，可以直接从字符串池里拿来使用，避免频繁的创建和销毁，提升效率和节约内存.

```py
# 面试扩展
str1 = "Hello"
str2 = "Hello"
str3 = "Hello"

# id()函数可以返回对象/数据的内存地址
print("str1的地址：", id(str1))  # str1的地址： 2179065101488
print("str2的地址：", id(str2))  # str2的地址： 2179065101488
print("str3的地址：", id(str3))  # str3的地址： 2179065101488
```



## 五、数据类型转换

### 5.1 隐式类型转换

> 代码演示

```py
var1 = 10
print("var1的类型：", type(var1))  # var1的类型： <class 'int'>

var2 = 1.1
print("var2的类型：", type(var2))  # var2的类型： <class 'float'>

# 类型转换
var3 = var1 + var2
print("var3 = ", var3, "var3的类型：", type(var3))  # var3 =  11.1 var3的类型： <class 'float'>
```



### 5.2 显示类型转换

> 代码演示

```py
n1 = 10
print("n1的类型：", type(n1))  # n1的类型： <class 'int'>

n2 = float(n1)
print("n2的类型：", type(n2))  # n2的类型： <class 'float'>

n3 = str(n1)
print("n3的类型：", type(n3))  # n3的类型： <class 'str'>
```

> 注意事项

```py
a = 100
b = 10.01

# 1、不管什么值的int,float都可以转成str,str(x)将对象 x 转换为字符串.
print(a, type(a), str(a), type(str(a)))  # 100 <class 'int'> 100 <class 'str'>
print(b, type(b), str(b), type(str(b)))  # 10.01 <class 'float'> 10.01 <class 'str'>

# 2、int转成float时,会增加小数部分,float转成int时,会去掉小数部分.
print(a, float(a))  # 100 100.0
print(b, int(b))  # 10.01 10

# 3、str转int,float使用int(x),float(x)将对象 x 转换为int/float.
x = "12.3"
print(x, type(x), float(x), type(float(x)))  # 12.3 <class 'str'> 12.3 <class 'float'>
y = "123"
print(y, type(y), int(y), type(int(y)))  # 123 <class 'str'> 123 <class 'int'>

# 4、在将str类型转为基本数据类型时，要确保str值能够转为有效数据，如果格式不正确，程序会报ValueError.
n4 = "12.3"
print(float(n4))  # 12.3
# print(int(n4)) # ValueError
n5 = "hello"
# print(float(n5)) # ValueError
# print(int(n5)) # ValueError

# 5、对一个变量进行强制转换后，会返回一个数据/值，但是并不会改变原变量的数据/值.
n6 = 10
n7 = float(n6)
print(n6, type(n6))  # 10 <class 'int'>
print(n7, type(n7), type(n6))  # 10.0 <class 'float'> <class 'int'>
```



## 六、小结

> 1. 程序阅读题，看看输出什么.

```py
n1 = 13
n2 = 17
n3 = n1 + n2
print("n3 =", n3)  # n3 = 30

n4 = 38
n5 = n4 - n3
print("n5 =", n5)  # n5 = 8
```

> 2. 使用str类型，分别保存\n\t\r\\1 2 3等字符，并打印输出.

```py
str1 = '\n'
str2 = '\t'
str3 = '\r'
str4 = '\\'
str5 = '1'

print(r"\n的效果：", str1)
print(r"\t的效果：", str2)
print(r"\r的效果：", str3)
print(r"\\的效果：", str4)
print(r"1的效果：", str5)
```

> 3. 保存两本书名，用+拼接;保存两本书价格，用加号拼接.

```py
book1_name = "西游记"
book1_price = 89.90
book2_name = "红楼梦"
book2_price = 139.70

print(book1_name + book2_name)
print(book1_price + book2_price)
```

> 4. 编程实现如下效果:
>
> 	姓名  年龄  成绩  性别  爱好
>
> 	XX   XX   XX   XX   XX
> 	要求：
>
> 	1. 用变量将姓名、年龄、成绩、性别、爱好存储;
> 	2. 使用+;
> 	3. 添加适当的注释;
> 	4. 添加转义字符，使用一条语句输出.

```py
# 定义变量
name = "jocker"
age = 18
score = 90.0
gender = "男"
hobby = "打胶"

# 按需求输出信息
print("姓名\t\t年龄\t\t成绩\t\t性别\t\t爱好\n" + name + '\t' + str(age) + '\t\t' + str(score) + '\t' + gender + '\t\t' + hobby)
```







# :symbols: 运算符



## 一、算术运算符

> 算术运算符：
>
> +加, -减, *乘, /除, %取余, //取整除, **幂.

```py
# 对于 a/b ,返回结果是小数
print(10 / 3)  # 3.3333333333333335

# 对于 a//b ,返回商的整数部分(向下取整)
print(10 // 3)  # 3
print(-10 // 3)  # -4

# 对于 a%b ,对应公式：a % b = a - a // b * b
print(10 % 3)  # 1
print(-10 % 3)  # 2
print(10 % -3)  # -2
print(-10 % -3)  # -1

# 对于 a**b ,返回a的b次方
print(2 ** 5)  # 32
```

> 代码演示

```py
# 1、假如还有97天放假，问：合xx个星期零xx天.
days = 97
week = days // 7
free_day = days % 7
print(f"假如还有{days}天放假,还有{week}个星期{free_day}天")

# 2、定义一个变量保存华氏温度，华氏温度转换摄氏温度的公式为：5/9（华氏温-100），请求出华氏温度对应的摄氏温度[234.5].
hua_shi = 234.5
she_shi = 5 / 9 * (hua_shi - 100)
print(f"华氏温度 {hua_shi} 对应的摄氏温度为 {she_shi} ")
print("华氏温度 %.2f 对应的摄氏温度为 %.2f" % (hua_shi, she_shi))
```



## 二、比较运算符

> 比较运算符：
>
> ==等于, !=不等于, <小于, >大于, <=小于等于, >=大于等于, is判断两个变量引用对象是否相同, is not判断两个变量引用对象是否不同.

```py
a = 10
b = 1
print(a > b)  # True
print(a >= b)  # True
print(a < b)  # False
print(a <= b)  # False
print(a == b)  # False
print(a != b)  # True

flag = a > b
print("flag =", flag)  # flag = True
print(a is b)  # False
print(a is not b)  # True
```



> Tips：== 与 is 的区别?

- 检查 a is b 的时候，其实相当于检查 id(a) == id(b).
- 检查 a == b 的时候，实际是调用了对象 a 的__eq()__ 方法，a == b 相当于 a.__eq__(b).
- is 是比 == 更严格的检查，只要 a 和 b 的值相等，a == b 就会返回True，
- 而只有 id(a) 和 id(b) 相等时，a is b 才返回 True.

```py
a = "hello"
b = "hello"
print(id(a))
print(id(b))
print(a is b)  # 输出 True
print(a == b)  # 输出 True

a = "hello world"
b = "hello world"
print(id(a))
print(id(b))
# Python中当字符串中出现了非标识符允许的字符的时候不采取驻留，即空格，如果把"hello world"改成"hello_world"， 在cmd命令下a is b还是返回 true，只是因为字符中存在一个空格所以才不采用驻留机制.
print(a is b)  # 注意：在Pycharm中返回True，在cmd命令行下会返回False,其指向的内存地址也会不同,这是因为Pycharm对Python的字符串驻留机制进行了优化.
print(a == b)  # 输出 True

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a is b)  # 输出 False
print(a == b)  # 输出 True

a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(a is b)  # 输出 True
print(a == b)  # 输出 True
```



## 三、逻辑运算符

> 逻辑运算符：
>
> and与, or或, not非.

```py
# 定义变量
a = 10
b = 20
c = 0

# 对于x and y,如果x为False,x and y返回x的值，否则返回y的计算值
print(a and b)  # 20
print(c and b)  # 0

# 对于x or y,如果x是True,它返回x的值，否则它返回 y的计算值
print(a or b)  # 10
print(c or b)  # 20

# 对于not x,如果x为True,返回 False，如果x为False，则返回 True
print(not (a and b))  # False
```



## 四、赋值运算符

> 赋值运算符：
>
> =赋值, +=复合加法赋值, -=复合减法赋值, *=复合乘法赋值, /=复合除法赋值, %=复合取模赋值, **=复合幂赋值, //=复合取整除赋值.

```py
# c = a + b 将 a + b的运算结果赋值为c
c = 10 + 20
print(c)  # 30

# c += a 等效于 c = c + a
c += 10
print(c)  # c = 30 + 10 = 40

# c -=a 等效于 c = c - a
c -= 20
print(c)  # c = 40 - 20 = 20

# c *= a 等效于 c = c * a
c *= 10
print(c)  # c = 20 * 10 = 200

# c /= a 等效于 c = c / a
c /= 10
print(c)  # c = 200 / 10 = 20.0

# c %= a 等效于 c= c % a
c %= 3
print(c)  # c = 20.0 % 3 = 2.0

# c **= a 等效于 c = c ** a
c **= 4
print(c)  # c = 2.0 ** 4 = 16.0

# c //= a 等效于 c = c // a
c //= 5
print(c)  # c = 16.0 // 5 = 3.0
```

> 需求：有两个变量，a 和 b，需求：将二者的值交换并打印结果.

```py
a = 30
b = 40

# ①使用中间变量来实现变量交换
print(f"未交换前 a={a},b={b}")  # 未交换前 a=30,b=40
temp = a
a = b
b = temp
print(f"交换后 a={a},b={b}")  # 交换后 a=40,b=30

# ②在Python中支持一个简单的实现变量交换方式：x,y = y,x
print(f"未交换前 a={a},b={b}")  # 未交换前 a=30,b=40
a, b = b, a
print(f"交换后 a={a},b={b}")  # 交换后 a=40,b=30

# ③不使用中间变量
print(f"未交换前 a={a},b={b}")  # 未交换前 a=30,b=40
a = a + b
b = a - b  # b = (a + b) - b = a
a = a - b  # a = (a + b) - a = b
print(f"交换后 a={a},b={b}")  # 交换后 a=40,b=30
```



## 五、三元运算符

> 三元运算符：
>
> Python是一种极简主义的编程语言，它没有引入?：这个运算符，而是使用if else关键字来实现相同的功能.
>
> 语法是：max = a if a > b else b.
>
> 1. 如果 a > b成立，就把a作为整个表达式的值，并赋给变量max;
> 2. 如果 a > b不成立，就把b作为整个表达式的值，并赋给变量max.

```py
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
```



## 六、运算符优先级

> 以下为运算符优先级：从上到下由高到低



## 七、标识符

- Python对各种变量、函数和类等命名时使用的字符序列称为标识符

> 命名规则

1. 由26个英文字母大小写，0-9，_组成;
2. 数字不可以开头;
3. 不可以使用关键字，但能包含关键字;
4. Python区分大小写;
5. 标识符中不能包含空格.

> 命名规范

- 变量名

	1. 变量要小写，若有多个单词，使用下划线分开;
	2. 常量全部大写;


- 函数名

	3. 函数名一律小写，如果有多个单词，用下划线隔开;

4. 私有函数以双下划线开头;

- 类名
	5. 使用大驼峰命名法(多个单词的首字母用大写开头，比如：MyName;扩展：小驼峰命名，第1个单词的首字母小写，后面的单词首字母都大写，例如：myName).



## 八、关键字







# :level_slider: 进制





# :control_knobs: 程序控制结构





# :repeat: 函数







# :package: 数据容器



## 一、数据容器概述

> **为什么需要数据容器？**

```python
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
# Python内置函数round(number, ndigits=None)作用:返回 number 舍入到小数点后 ndigits 位精度的值.如果 ndigits 被省略或为 None，则返回最接近输入值的整数
# https://docs.python.org/zh-cn/3.11/library/functions.html#round
print(round(25.567, 2))  # 25.57
print(f"总体重是:{total_weight},平均体重是:{round(avg_weight, 1)}")  # 总体重是:64.4,平均体重是:10.7
```



> **什么是数据容器**

### 1.1 基本介绍

1. 数据容器是一种数据类型，有些地方也简称为容器/collections.
2. 数据容器可以存放多个数据，每一个数据也被称为一个元素.
3. 存放的数据/元素可以是任意类型.
4. 简单的说，数据容器就是一种可以存放多个数据/元素的数据类型.



### 1.2 容器分类

1. [列表(list)](https://docs.python.org/zh-cn/3.11/library/stdtypes.html#list)
2. [元组(tuple)](https://docs.python.org/zh-cn/3.11/library/stdtypes.html#tuple)
3. [字符串(str)](https://docs.python.org/zh-cn/3.11/library/stdtypes.html#str)
4. [集合(set)](https://docs.python.org/zh-cn/3.11/library/stdtypes.html#set)
5. [字典(dict)](https://docs.python.org/zh-cn/3.11/library/stdtypes.html#dict)



## 二、容器1——列表[list]

### 2.1 基本介绍

1. 列表可以存放多个不同类型数据，即：列表就是一列数据(多个数据).

2. 列表也是一种数据类型.

> 列表的定义

```python
# 创建一个列表，只要用逗号分隔的不同的数据项使用方括号括起来即可:
list1 = [100, 200, 300, 400, 500]
list2 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
```

> 列表的使用

```python
# 列表名[索引]
print(list1)  # [100, 200, 300, 400, 500]
print(type(list1))  # <class 'list'>
print(list1[0])  # 100
print(list1[4])  # 500
# print(list1[5])  # IndexError

# Python内置函数len():返回对象的长度(元素个数)
print(len(list1))  # 5
```

> 列表的遍历

```python
# 将列表的每个元素依次取出，进行处理的操作，就是遍历/迭代

# while遍历列表
index = 0
while index < len(list1):
    print(f"第{index + 1}个元素是:{list1[index]}")
    index += 1
"""
Console Result:
第1个元素是:100
第2个元素是:200
第3个元素是:300
第4个元素是:400
第5个元素是:500
"""

# for遍历列表
for i in list1:
    print(i)
"""
Console Result:
100
200
300
400
500
"""
```

> 代码实现————使用列表(list)解决养鸡场问题

```python
# 使用数据容器-列表,接收所有小鸡体重
list2 = [3, 5, 1, 3.4, 2, 50]

# 初始化总体重
total_weight = 0.0

# 遍历列表并将体重累加到总体重total_weight变量上
for i in list2:
    total_weight += i
    
# 平均体重
avg_weight = total_weight / len(list2)
print(f"总体重是:{total_weight},平均体重是:{round(avg_weight, 1)}")
```



### 2.2 注意事项

```python
# 1、如果我们需要一个空列表，可以通过list_test = [] 或 list_test = list()方式来定义
list1 = []
list2 = list()
print(list1, type(list1))  # [] <class 'list'>
print(list2, type(list2))  # [] <class 'list'>

# 2、列表的元素可以有多个，而且数据类型没有限制，允许有重复元素，并且是有序的
list3 = [100, 'jack', 4.5, True]
print(list3)
# 嵌套列表
list4 = [100, 'tom', ['jack', '呵呵', 300]]
print(list4)

# 3、列表的索引/下标是从0开始的

# 4、列表索引必须在指定范围内使用，否则报：IndexError:list index out of range
list5 = [10, 20, 30]  # 有效索引/下标是0-2
# print(list5[3])  # IndexError

# 5、索引也可以从尾部开始，最后一个元素的索引为-1，往前一位为-2，以此类推
print(list5[-1])  # 30
print(list5[2])  # 30

# 6、通过列表[索引]=新值对数据进行更新，使用list.append(值)方法来添加元素，使用del语句来删除列表的元素，注意不能超出有效索引范围
# 通过index修改原索引下的列表值
list5[0] = "小乔"
print(list5)  # ['小乔', 20, 30]

# 通过append方法在旧列表后追加新值
list5.append("兰陵王")
print(list5)  # ['小乔', 20, 30, '兰陵王']

# 通过del语句删除指定索引下的列表值
del list5[2]
print(list5)  # ['小乔', 20, '兰陵王']

# 7、列表是可变序列（要注意其使用特点)
list6 = [1, 3, 5.6]
print(list6[2], id(list6[2]))  # 5.6 2248170988080
print(f"list:{list6} 地址:{id(list6)}")  # list:[1, 3, 5.6] 地址:1536484673472

# 列表的元素是可以修改的，修改后，列表变量指向地址不变，只是数据内容变化
list6[2] = 4
print(list6[2], id(list6[2]))  # 2248169947472
print(f"list:{list6} 地址:{id(list6)}")  # list:[1, 3, 4] 地址:1536484673472

# 扩展
list8 = [3, 4, 5]
list7 = list8
list7[0] = 500
print("list7 =", list7)  # list7 = [500, 4, 5]
print("list8 =", list8)  # list8 = [500, 4, 5]
```



### 2.3 常用操作

> 列表常用操作

| 序号 | 函数或方法                                                   |
| :--: | :----------------------------------------------------------- |
|  1   | len(list):返回列表元素个数.                                  |
|  2   | max(list):返回列表元素最大值.                                |
|  3   | min(list):返回列表元素最小值.                                |
|  4   | list(tuple):将元组转换为列表.                                |
|  5   | list.append(obj):在列表末尾添加新的对象.                     |
|  6   | list.count(obj):统计某个元素在列表中出现的次数.              |
|  7   | list.extend(seq):在列表末尾一次性追加另一个序列中的多个值(用新列表扩展原列表). |
|  8   | list.index(obj):从列表中找出某个值第一个匹配项的索引值.      |
|  9   | list.insert(index, obj):将对象插入列表.                      |
|  10  | list.pop([index = -1]):移除列表中的一个元素(默认最后一个元素),并且返回该元素的值. |
|  11  | list.remove(obj):移除列表中某个值的第一个匹配项.             |
|  12  | list.reverse():反转列表元素.                                 |
|  13  | list.sort(key = None, reverse = False):对原列表进行排序.     |
|  14  | list.clear():清空列表.                                       |
|  15  | list.copy():复制列表.                                        |

> 代码演示

```py
# 定义列表list1
list1 = [100, 200, 300, 500, 800]
# len函数获取元素个数
print(len(list1))  # 5

# max函数获取最大值
print(max(list1))  # 800

# min函数获取最小值
print(min(list1))  # 100

# append方法追加对象
list1.append(1300)
print(list1)  # [100, 200, 300, 500, 800, 1300]

# count方法获取某个元素出现的次数
print(list1.count(500))  # 1

# extend方法追加多个对象
list2 = [2100, 3400]
list1.extend(list2)
print(list1)  # [100, 200, 300, 500, 800, 1300, 2100, 3400]

# index方法获取对象第一次出现的索引值
print(list1.index(2100))  # 6

# reverse方法反转列表
list1.reverse()
print(list1)  # [3400, 2100, 1300, 800, 500, 300, 200, 100]

# insert方法将对象插入到指定索引位置,后面的对象对应的索引值+1
list1.insert(2, "李白")
print(list1)  # [3400, 2100, '李白', 1300, 800, 500, 300, 200, 100]
```



### 2.4 列表生成式

1. 列表生成式就是"生成列表的公式".

2. 基本语法

	[列表元素的表达式 for 自定义变量 in 可迭代对象]

	如:[i * 2 for i in range(1, 5)] -> 得到列表[2, 4, 6, 8]

	list = [i + i for i in "Simon"] -> 得到列表['SS', 'ii', 'mm', 'oo', 'nn']

> 代码演示

```py
"""
需求:生成一个列表，内容为[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
list1 = [i ** 2 for i in range(1, 11)]
print(list1)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```



### 2.5 列表Demo

> 代码实现————循环从键盘输入5个成绩，保存列表并输出

```py
# 定义空列表list_score
list_score = []

# 从控制台中遍历并接收数据
for i in range(5):
    score = float(input(f"请输入第{i + 1}个成绩:"))
    list_score.append(score)
print("5个学生的成绩为:", list_score)
```



## 三、容器2——元组(tuple)

### 3.1 基本介绍

1. 元组(tuple)可以存放多个不同类型的数据**,**元组是不可变序列.

	注意:tuple不可变是指当你创建tuple后,它就无法改变,也没有append、insert方法,虽有获取索引值的方法,但是不能重新赋值.

2. 元组也是一种数据类型.

> 元组的定义

```py
# 创建一个元组,只要把逗号分隔的不同的数据项,使用圆括号括起来即可:
list1 = (100, 200, 300, 400, 500)
list2 = ('red', 'green', 'blue', 'yellow', 'white', 'black')
```

> 元组的使用

```py
# 元组名[索引]
list1 = (100, 200, 300, 400, 500)
print(f"元组的内容是:{list1} 类型是:{type(list1)}")  # 元组的内容是:(100, 200, 300, 400, 500) 类型是:<class 'tuple'>
print(list1[2])  # 300
```

> 元组的遍历([用法与列表一致](# 2.1 基本介绍))

```py
# 将元组的每个元素依次取出，进行处理的操作，就是遍历/迭代
```

> Tips:列表操作起来更加方便,那么元组相较于列表的优势？

- 在项目中，尤其是多线程环境中，有经验的程序员会考虑不变对象(一方面因为对象状态不能修改，所以可以避免由此引起的不必要的程序错误；另一方面一个不变对象自动就是线程安全的，这样就可以省掉处理同步化的开销。可以方便的被共享访问)。所以，如果不需要对元素进行增删改操作的话使用元组.
- 元组在创建时间和占用的空间上面都优于列表.
- 元组能够对不需要修改的数据保护.

### 3.2 注意事项

```py
# 1、如果我们需要一个空元组，可以通过tuple_test = ()，或者tuple_test = tuple()方式来定义 (与列表类似)

# 2、元组的元素可以有多个，而且数据类型没有限制，允许有重复元素，并且是有序的 (与列表类似)

# 3、元组的索引/下标是从0开始的 (与列表类似)

# 4、元组索引必须在指定范围内使用，否则报：IndexError:tuple index out of range (与列表类似)

# 5、索引也可以从尾部开始，最后一个元素的索引为-1，往前一位为-2，以此类推 (与列表类似)

# 6、元组是不可变序列 (区别与列表是可变序列)
tuple1 = (1, 2, 3)
# tuple1[0] = 100  # TypeError
print(tuple1)

# 7、但是可以修改元组内list的内容(增删改均可)
tuple2 = (1, 3, [5, 7, "张飞"], "牛魔")
print(tuple2)  # (1, 3, [5, 7, '张飞'], '牛魔')
# 修改
tuple2[2][1] = "李信"
print(tuple2)  # (1, 3, [5, '李信', '张飞'], '牛魔')
# 删除
del tuple2[2][0]
print(tuple2)  # (1, 3, ['李信', '张飞'], '牛魔')
# 增加
tuple2[2].append("大乔")
print(tuple2)  # (1, 3, ['李信', '张飞', '大乔'], '牛魔')

# 8、定义只有一个元素的元组,需要带上逗号,否则会被识别为int、str等其它类型
tuple3 = (100)
tuple4 = (100,)
print(f"tuple3的类型是{type(tuple3)}")  # tuple3的类型是<class 'int'>
print(f"tuple4的类型是{type(tuple4)}")  # tuple4的类型是<class 'tuple'>
```



### 3.3 常用操作

> 元组常用操作([用法与列表类似](# 2.3 常用操作))

| 序号 | 函数或方法                                               |
| :--: | -------------------------------------------------------- |
|  1   | len(tuple):返回元组元素个数.                             |
|  2   | max(tuple):返回元组元素最大值.                           |
|  3   | min(tuple):返回元组元素最小值.                           |
|  4   | tuple.count(obj):统计某个元素在元组中出现的次数.         |
|  5   | tuple.index(obj):从元组中找出某个值第一个匹配项的索引值. |



### 3.4 元组Demo

> 代码实现————定义一个元组，('大话西游','周星驰',80,['周星驰','小甜甜']),信息为(片名,导演,票价,演员列表)
>
> 1. 查询票价对应的索引;
> 2. 遍历所有演员;
> 3. 删除’小甜甜‘，增加演员'牛魔王'、’猪八戒‘.

```py
# 定义元组tuple1
tuple1 = ('大话西游', '周星驰', 80, ['周星驰', '小甜甜'])

# 1. 查询票价对应的索引
print(tuple1.index(80))  # 2

# 2. 遍历所有演员
for i in tuple1[3]:
    print(i)
    
# 3. 删除’小甜甜‘
del tuple1[3][1]
print(tuple1)  # ('大话西游', '周星驰', 80, ['周星驰'])

# 4. 增加演员'牛魔王'、'猪八戒'
list1 = ['牛魔王', '猪八戒']
tuple1[3].extend(list1)
print(tuple1)  # ('大话西游', '周星驰', 80, ['周星驰', '牛魔王', '猪八戒'])
```



## 四、容器3——字符串“str”

### 4.1 基本介绍

1. 在Python中处理文本数据是使用str对象,也称为字符串.字符串是由Unicode编码构成的不可变序列.

	Unicode码是一种字符编码,相应的还有utf-8,gbk等.

	ord()函数 用于返回单个字符对应的unicode编码值.

2. 字符串字面值的三种写法

	单引号:'可以嵌入"双引号"'.

	双引号:"可以嵌入'单引号'".

	三重引号:‘‘‘三重单引号’’’,“““三重双引号”””.

3. 字符串是字符的容器,一个字符串可以存放多个字符.

> 字符串支持索引

```py
# 字符串名[索引]
str1 = "red - green"
print(str1[4])  # -
```

> 字符串的遍历([用法与列表一致](# 2.1 基本介绍))

```py
# 将字符串的每个元素依次取出，进行处理的操作，就是遍历/迭代
```



### 4.2 注意事项

```py
# 1、字符串索引必须在指定范围内使用，否则报：IndexError:tuple index out of range (与列表、元组特性一致)
# 2、字符串是不可变序列,不可修改 (与元组特性一致)
```



### 4.3 常用操作

| 序号 | 函数或方法                                                   |
| :--: | ------------------------------------------------------------ |
|  1   | len(str):字符串的长度,也就是包含多少个字符.                  |
|  2   | str.replace(old, new[,count]):返回字符串的副本,其中出现的所有子字符串old替换为new,可选参数count:替换前count个. |
|  3   | str.split(sep = None, maxsplit = -1):返回一个有字符串内单词组成的列表,使用sep作为分隔字符串.如果给出了maxsplit，则最多进行 maxsplit 次拆分（因此，列表最多会有 maxsplit+1 个元素）.如果 maxsplit 未指定或为 -1，则不限制拆分次数（进行所有可能的拆分）. |
|  4   | str.count(sub):统计指定字符串在字符串中出现的次数.           |
|  5   | str.index(sub):从字符串中找出指定字符串第一个匹配项的索引值. |
|  6   | str.strip([chars]):返回原字符串的副本，移除其中的前导和末尾字符.chars参数为指定要移除字符的字符串.一般用于去除前后空格或指定字符串. |
|  7   | str.lower():返回原字符串小写的副本.                          |
|  8   | str.upper():返回原字符串大写的副本.                          |

> 代码演示

```py
# 定义字符串
str1 = "Xiang lin is name is Simon lin"
print(str1)

# len()函数
print(len(str1))  # 30

# replace方法
new_str = str1.replace('lin', '林', 1)
print(new_str)  # Xiang 林 is name is Simon lin

# split方法
str_split = str1.split(" ", -1)
print(str_split, type(str_split))  # ['Xiang', 'lin', 'is', 'name', 'is', 'Simon', 'lin'] <class 'list'>

# count方法
print(str1.count('is'))  # 2

# index方法
print(str1.index('name'))  # 13

# strip方法
# 去除前后空格
str2 = '   hello world   '.strip(" ")
print(str2)  # hello world
# 去除指定字符串
str3 = ' tth heel th fire tht '.strip(" th")  # 去除字符串前后所有的' ','t','h'字符,不论顺序先后
print(str3)  # eel th fire

# lower方法
str4 = str1.lower()
print(str4)  # xiang lin is name is simon lin

# upper方法
str5 = str1.upper()
print(str5)  # XIANG LIN IS NAME IS SIMON LIN
```



### 4.4 字符串比较

1. 运算符: >, >=, <, <=, ==, !=.

2. 比较规则:首先比较两个字符串中的第一个字符,如果相等则继续比较下一个字符,依次比较下去,直到不等时,就是比较结果.

3. 比较原理:依据字符对应的ordinal value,也就是码值大小来判定 (Unicode码值上限65536).

	`ord()`函数用于将字符转换为码值.

	`chr()`函数用于将码值转换为字符.

> 代码演示

```py
print(ord('9'))  # 57
print(ord('瑶'))  # 29814

print(chr(57))  # 9
print(chr(29814))  # 瑶

print('tom' > 'jack')  # True
```



### 4.5 字符串Demo

> 代码实现————定义一个字符串,str_names = "tom jack mary nono smith hsp",
>
> 1. 统计一共有多少人名;
> 2. 如果有'hsp',替换为'老韩';
> 3. 如果人名是英文,把首字母改为大写.

```py
# 定义字符串str_names
str_names = "tom jack mary nono smith hsp"

# 使用split方法分隔字符串并返回一个列表
list1 = str_names.split(" ")
print(list1)  # ['tom', 'jack', 'mary', 'nono', 'smith', 'hsp']

# 1. 统计一共有多少人名
print(len(list1))  # 6

# 2. 如果有'hsp',替换为'老韩'
str1 = str_names.replace('hsp', '老韩')
print(str1)  # tom jack mary nono smith 老韩

# 3. 如果人名是英文,把首字母改为大写
str2 = ""
print(id(str2))  # 1673854943280
for i in list1:
    # isalpha方法:如果字符串中的所有字符都为字符并且至少有一个字符则返回True,否则返回False.用于筛选出英文名
    if i.isalpha():
        # capitalize方法:返回原字符串的副本,首字符大写,其余小写.
        # 将list1中遍历的元素追加到空字符串str2中,并以" "符号间隔
        str2 += i.capitalize() + " "
        print(id(str2))
# 注意:字符串虽然是不可变序列,但通过id()函数可观察到str2每次加入元素内存地址都会变化;
# 说明str2字符串名虽然未变,但每次遍历之后都是新的对象.
print(str2.strip())  # Tom Jack Mary Nono Smith Hsp
print(id(str2.strip()))  # 2848325705504
```



### 4.6 切片操作

> 基本介绍

1. 切片:从一个序列中,取出一个子序列.
2. 序列:内容连续、有序,可使用索引的一类数据容器.
3. 列表(list)、元组(tuple)、字符串均可视为序列.

>基本语法————序列[起始索引:结束索引:步长]

1. 表示从序列中,从指定的起始索引开始,按照指定的步长,依次取出元素,到指定结束索引为止,截取到一个新的序列.

2. 切片操作是 前闭后开 ,即[起始索引:结束索引).

3. 步长表示:依次取出元素的间隔.

	步长为1:每次跳过0个元素取值,即:每个元素都取出.同时也是默认值;

	步长为2:每次跳过1个元素取值;

	步长为N:每次跳过N-1个元素取值.

> 代码演示

```py
# 注意:切片当中的符号是冒号: 而不是逗号,

# 对字符串进行切片
str1 = "hello,world"
# 截取hello
str_slice = str1[0:5]
print(str_slice)  # hello

# 对列表进行切片
list1 = ["hello", "jack", "tom", "simon"]
# 截取["jack", "simon"]
list_slice = list1[1:4:2]
print(list_slice)  # ['jack', 'simon']

# 对元组进行切片
tuple1 = (100, 300, 700, 1000, 3000)
# 截取(300, 700, 1000, 3000)
tuple_slice = tuple1[1:5]
print(tuple_slice)  # (300, 700, 1000, 3000)
```

> 注意事项

```py
str2 = "hello,world"

# 1. 起始索引默认从0开始,结束索引默认截取到结尾,步长默认为1
str2_a = str2[:5:1]
print(str2_a)  # hello

str2_b = str2[1::1]
print(str2_b)  # ello,world

str2_c = str2[::2]
print(str2_c)  # hlowrd

str2_d = str2[2:7:]
print(str2_d)  # llo,w

# 2. 步长为负时,表示反向取值,同时起始索引和结束索引的默认值也变为了-1和-总长
str2_e = str2[::-1]
print(str2_e)  # dlrow,olleh

str2_f = str2[-1:-6:-1]
print(str2_f)  # dlrow

# 3. 切片操作并不会影响原序列,而是返回了一个新序列
```

> 切片Demo————定义列表list_name = ["Jack", "Lisa", "Hsp", "Paul", "Simon", "Kobe"]
>
> 1. 取出前三个名字;
> 2. 取出后三个名字,并且保证原来的顺序.

```py
# 定义列表list_name
list_name = ["Jack", "Lisa", "Hsp", "Paul", "Simon", "Kobe"]

# 1. 取出前三个名字
list1 = list_name[:3:]
print(list1)  # ['Jack', 'Lisa', 'Hsp']

# 2. 取出后三个名字,并且保证原来的顺序
list2 = list_name[:-4:-1]
print(list2)  # ['Kobe', 'Simon', 'Paul']

# ① 使用reverse反转列表元素
list2.reverse()
print(list2)  # ['Paul', 'Simon', 'Kobe']
# ② 使用切片再次逆序
list3 = list2[::-1]
print(list3)  # ['Paul', 'Simon', 'Kobe']
```



## 五、容器4——集合{set}

### 5.1 基本介绍

1. Python支持集合这种数据类型,集合是由不重复元素组成的无序容器.

2. 集合对象支持合集、交集、差集等数学运算.

> 集合的定义

```py
# 创建一个集合,只要用逗号分隔不同的数据项,并用{}括起来即可,如:
set_a = {100, 200, 300}

# 集合是无序的
print(f"{set_a},{type(set_a)}")  # {200, 100, 300},<class 'set'>
```

> Tips:既然有了列表、元组这样的数据容器,为什么还提供集合？

- 在项目中,可能有这样的需求:需要记录一些数据,而这些数据必须保证是不重复的,而且数据的顺序没有要求,这样就可以使用集合.
- 列表、元组的元素是可以重复的,而且有序;而集合不可重复且无序.



### 5.2 注意事项

```py
# 1、集合是由不重复元素组成的无序容器
# 无序,也就是定义元素的顺序和取出的顺序不能保证一致
# 集合底层会按照自己的一套算法来存储和取数据,所以每次取出顺序不变
set_b = {100, 100, 400, 600, 500, 400}
print(set_b)  # {400, 600, 100, 500}
print(set_b)  # {400, 600, 100, 500}
print(set_b)  # {400, 600, 100, 500}

# 2、集合不支持索引
# print(set_b[0])  # 抛出TypeError异常

# 3、既然集合不支持索引,所以对集合进行遍历不支持while,只支持for
# for循环遍历set集合
for i in set_b:
    print(i)

# 4、创建空集合只能用set_test = set(),不能用{},{}创建的是空字典
set_c = {}  # dict类型
set_d = set()  # set类型
print(f"{type(set_c)},{type(set_d)}")  # <class 'dict'>,<class 'set'>
```



### 5.3 常用操作

> 集合常用操作

| 序号 | 函数或方法                                                   |
| :--: | ------------------------------------------------------------ |
|  1   | len(set):获取集合元素个数.                                   |
|  2   | x in s:检测元素x是否为集合s中的成员.                         |
|  3   | set.add(i):将元素i添加到集合中.                              |
|  4   | set.remove(i):移除元素i,如果不存在则抛出KeyError异常.        |
|  5   | set.pop():移除并返回任意一个元素,如果为空抛出KeyError异常.   |
|  6   | set.clear():移除所有元素.                                    |
|  7   | union(*others) set\|other\|…:返回一个新集合,其中包含来自原集合以及others指定的所有集合中的元素. |
|  8   | intersection(*others) set&other&...:返回一个新集合,其中包含来自原集合以及others指定的所有集合中共有的元素. |
|  9   | difference(*others) set-other-...:返回一个新集合,其中包含来自原集合以及others指定的其它集合中不存在的元素. |

> 代码演示

```py
# 定义集合
set_a = {'TikTok', 'Facebook', 'Twitter', 'Telegram', 'Facebook', 'Twitter'}

# len
print(len(set_a))  # 4

# x in s
print("Facebook" in set_a)  # True

# add
set_a.add("WeChat")
print(set_a)  # {'WeChat', 'Twitter', 'Facebook', 'Telegram', 'TikTok'}

# remove
set_a.remove("TikTok")
print(set_a)  # {'Facebook', 'Telegram', 'WeChat', 'Twitter'}

# pop, 注:pop操作会影响到原集合
set_a.pop()
print(set_a)  # {'WeChat', 'Telegram', 'Twitter'}

# clear

# 定义两个集合apps，apps2
apps = {'WeChat', 'Telegram', 'Twitter'}
apps2 = {'Twitter', 'Facebook', 'Telegram', 'TikTok'}
# union,相当于数学中的合集(并集),即:将集合A和B合并并组成新的集合
apps3 = apps | apps2  # 等价于apps3 = apps.union(apps2)
print(apps3)  # {'Twitter', 'WeChat', 'Facebook', 'TikTok', 'Telegram'}

# intersection,相当于数学中的交集,即:将集合A和B共有的元素取出并组成新的集合
apps4 = apps & apps2  # 等价于apps4 = apps.intersection(apps2)
print(apps4)  # {'Twitter', 'Telegram'}

# difference,相当于数学中的差集,即:将只存在于集合A中的元素取出并组成新的集合
apps5 = apps - apps2  # 等价于apps5 = apps.difference(apps2)
print(apps5)  # {'WeChat'}
```



### 5.4 集合生成式

1. 集合生成式就是"生成集合的公式"

2. 基本语法

	{集合元素的表达式 for 自定义变量 in 可迭代对象}

	如:{i * 2 for i in range(1, 5)} -> 得到集合{2, 4, 6, 8}

3. 用法参考[列表生成式](# 2.4 列表生成式)



### 5.5 集合Demo

> 代码实现————用三个集合表示三门学科的选课学生姓名(一个学生可以同时选多门课)
>
> s_history = {'小明', '张三', '李四', '王五', 'Lily', 'Bob'}
>
> s_politic = {'小明', '小花', '小红', '一狗'}
>
> s_english = {'小明', 'Lily', 'Bob', 'Davil', '李四'}
>
> 1. 求选课学生总共有多少人;
> 2. 求只选了第一个学科的学生数量和学生名字;
> 3. 求只选了一门学科的学生数量和学生名字;
> 4. 求选了三门学科的学生数量和学生名字.

```py
# 定义3个集合
s_history = {'小明', '张三', '李四', '王五', 'Lily', 'Bob'}
s_politic = {'小明', '小花', '小红', '一狗'}
s_english = {'小明', 'Lily', 'Bob', 'Davil', '李四'}

# 1. 求选课学生总共有多少人
s_count = s_english | s_politic | s_history
print(len(s_count))  # 10

# 2. 求只选了第一个学科的学生数量和学生名字
s_his = s_history - s_english - s_politic
print(len(s_his), s_his)  # 2 {'王五', '张三'}

# 3. 求只选了一门学科的学生数量和学生名字
# 分别求出只选择了各个学科的学生，然后求并集后自动去重
s_eng = s_english - s_politic - s_history
s_pol = s_politic - s_history - s_english
s_only = s_his | s_eng | s_pol
print(len(s_only), s_only)  # 6 {'小花', '小红', '张三', '一狗', 'Davil', '王五'}

# 4. 求选了三门学科的学生数量和学生名字
s_all = s_history & s_english & s_politic
print(len(s_all), s_all)  # 1 {'小明'}
```



## 六、容器5——字典{key:value}

> 需求:一个公司有多个员工，请使用合适的数据类型保存员工的信息(比如员工号、年龄、名字、入职时间、薪水等)，要求
>
> 1. 员工号是入职时分配的，唯一不重复;
> 2. 通过员工号，可以查询到员工的信息;
> 3. 根据需要，可以动态的增加、删除员工;
> 4. 根据需要，可以修改员工的信息(比如 年龄、名字、入职时间、薪水等).

- 像这种基于Key 查询Value 的场景需求,是一种映射关系.而列表,元组,集合都是一种单值存储,处理映射关系并不方便,由此便引入了字典dict.



### 6.1 基本介绍

1. 字典(dict, 全称dictionary)是一种常用的Python数据类型,在其他语言中可能把字典称为联合内存或联合数组.
2. 字典是一种映射类型,专门处理通过key查询Value的需求.

> 字典的定义

```py
# 创建一个字典,只要用逗号分隔的不同的元素,并用{}括起来即可,存储的元素称为键值对,如:
dict_a = {'key':'value', 'key':'value', 'key':'value'}
# 通过key取出对应的value: 字典名[key]

# 定义字典dict_a
dict_a = {'book': '编程', 'name': 'Python', 'price': 99.8}
print(type(dict_a))  # <class 'dict'>
print(dict_a['name'])  # Python
```



### 6.2 注意事项

```py
# 1、字典的Key通常是字符串或数字,Value可以是任何数据类型

# 2、字典不支持索引,否则会抛出KeyError异常

# 3、既然字典不支持索引,所以对字典进行遍历不支持while,只支持for.注:对字典进行遍历,遍历的对象是Key,而不是Key:Value
dict_b = {'a': 1, 'b': 2, 'c': 3}
# 获取value的3种方法
# 遍历方式①
for i in dict_b:
    print(f'key:{i},value:{dict_b[i]}')
'''
Console Result:
key:a,value:1
key:b,value:2
key:c,value:3
'''

# 遍历方式②
for i in dict_b.values():
    print(f'value:{i}')
'''
Console Result:
value:1
value:2
value:3
'''

# 遍历方式③
for i, j in dict_b.items():
    print(f'key:{i},value:{j}')
'''
Console Result:
key:a,value:1
key:b,value:2
key:c,value:3
'''

# 4、创建空字典:dict_test = {} 或 dict_test = dict()

# 5、字典的Key必须是唯一的,如果指定了多个相同的Key,后面的键值对会覆盖前面的
dict_c = {'a': 1, 'b': 2, 'c': 3, 'b': 200}
print(dict_c)  # {'a': 1, 'b': 200, 'c': 3}
```



### 6.3 常用操作

| 序号 | 函数或方法                                                   |
| :--: | ------------------------------------------------------------ |
|  1   | len(dict):返回字典的键值对个数.                              |
|  2   | d[key]:返回字典d中以key为键的value值,如果key值不存在则抛出KeyError异常. |
|  3   | d[key] = value:如果key值存在,修改原value值;反之,则是增加一个key-value键值对. |
|  4   | del d[key]:如果key值存在,移除该键值对;反之抛出异常.          |
|  5   | pop(key[,default]):如果key值存在,移除该键值对并返回value值;否则返回default;如果不给default且key值不存在,抛出异常. |
|  6   | keys():返回字典中所有的key值.                                |
|  7   | key in d:如果字典d中存在key值,返回True;否则返回False.        |
|  8   | clear():移除字典中所有的键值对.                              |

> 代码演示

```py
# 定义字典
dict_a = {'a': 1, 'b': 2, 'c': 3}

# len
print(len(dict_a))  # 3

# d[key]
print(dict_a['b'])  # 2

# d[key] = value
dict_a['b'] = 20
print(dict_a)  # {'a': 1, 'b': 20, 'c': 3}
dict_a['d'] = 4
print(dict_a)  # {'a': 1, 'b': 20, 'c': 3, 'd': 4}

# del d[key]
del dict_a['c']
print(dict_a)  # {'a': 1, 'b': 20, 'd': 4}

# pop(key[,default])
# key值存在
# val_new = dict_a.pop('d', 'hhh')
# print(val_new, dict_a)  # 4 {'a': 1, 'b': 20}
# key值不存在
val_new = dict_a.pop('e', 'hhh')
print(val_new, dict_a)  # hhh {'a': 1, 'b': 20, 'd': 4}

# keys()
dict_all = dict_a.keys()
print(dict_all, type(dict_all))  # dict_keys(['a', 'b', 'd']) <class 'dict_keys'>

# key in d
print('a' in dict_a)  # True
print('c' in dict_a)  # False

# clear()
dict_a.clear()
print(dict_a)  # {}
```



### 6.4 字典生成式

> 基本语法
>
> ​    `{字典key的表达式:字典value的表达式 for 表示key的变量,表示value的变量 in zip(可迭代对象,可迭代对象)}`
>
> 内置函数zip()
>
> ​    作用:zip()可以将可迭代的对象作为参数,将对象中对应的元素打包成一个元组,返回由这些元组组成的列表.

```py
"""
Demo1:给出了如下两个列表:
        books = ["红楼梦", "三国演义", "西游记", "水浒传"]
        authors = ["曹雪芹", "罗贯中", "吴承恩", "施耐庵"]
   生成对应的字典:
        {'红楼梦': '曹雪芹', '三国演义': '罗贯中', '西游记': '吴承恩', '水浒传': '施耐庵'}
"""
books = ["红楼梦", "三国演义", "西游记", "水浒传"]
authors = ["曹雪芹", "罗贯中", "吴承恩", "施耐庵"]

dict_b = {i: j for i, j in zip(books, authors)}
print(dict_b)  # {'红楼梦': '曹雪芹', '三国演义': '罗贯中', '西游记': '吴承恩', '水浒传': '施耐庵'}

# Demo2
str1 = 'Simon'
dict_c = {i: j * 2 for i, j in zip(str1, str1)}
print(dict_c)  # {'S': 'SS', 'i': 'ii', 'm': 'mm', 'o': 'oo', 'n': 'nn'}

"""
Demo3:给出两个列表:
english_list = ["red", "black", "yellow", "white"]
chinese_list = ["红色", "黑色", "黄色", "白色"]
生成一个字典:
{'红色': 'RED', '黑色': 'BLACK', '黄色': 'YELLOW', '白色': 'WHITE'}
"""
english_list = ["red", "black", "yellow", "white"]
chinese_list = ["红色", "黑色", "黄色", "白色"]
dict_d = {i: j.upper() for i, j in zip(chinese_list, english_list)}
print(dict_d)  # {'红色': 'RED', '黑色': 'BLACK', '黄色': 'YELLOW', '白色': 'WHITE'}
```



### 6.5 字典Demo

> 代码实现————员工信息管理问题
>
> 一个公司有多个员工，请使用合适的数据类型保存员工的信息(比如员工号、年龄、名字、入职时间、薪水等)，要求:
>
> 1. 员工号是入职时分配的，唯一不重复;
> 2. 通过员工号(0010)，可以查询到员工的信息;
> 3. 根据需要，可以动态的增加、删除员工;
> 4. 根据需要，可以修改员工的信息(比如 年龄、名字、入职时间、薪水等);
> 5. 遍历所有员工,把所有员工的薪水,提升20%;
> 6. 按照员工号为？？的信息如下:年龄：？？名字：？？入职时间：？？薪水：？？的格式输出员工信息.

```py
# 1、员工号是入职时分配的，唯一不重复
clerks = {
    '0001': {
        "age": 20,
        "name": "贾宝玉",
        "entry_time": "2011-11-11",
        "sal": 12000
    },
    '0002': {
        "age": 21,
        "name": "薛宝钗",
        "entry_time": "2015-12-12",
        "sal": 10000
    },
    '0010': {
        "age": 18,
        "name": "林黛玉",
        "entry_time": "2018-10-10",
        "sal": 20000
    }
}

# 2、通过员工号(0010)，可以查询到员工的信息
msg_0010 = clerks['0010']
print(
    f"员工号0010的员工信息:\n年龄:{msg_0010['age']}\n姓名:{msg_0010['name']}\n入职时间:{msg_0010['entry_time']}\n工资:{msg_0010['sal']}")

"""
Console Result:
员工号0010的员工信息:
年龄:18
姓名:林黛玉
入职时间:2018-10-10
工资:20000
"""

# 3、根据需要，可以动态的增加、删除员工
clerks['0020'] = {
    "age": 22,
    "name": "韩信",
    "entry_time": "2024-03-15",
    "sal": 50000
}
print(clerks)
del clerks['0002']
print(clerks)

# 4、根据需要，可以修改员工的信息(比如 年龄、名字、入职时间、薪水等)
# 方式①
clerks['0001'] = {
    "age": 25,
    "name": "宝玉",
    "entry_time": "2021-10-01",
    "sal": 22000
}
print(clerks)
# 方式②
clerks['0001']['age'] = 27
clerks['0001']['entry_time'] = "2023-10-01"
clerks['0001']['sal'] += clerks['0001']['sal'] * 0.1
print(clerks)

# 5、遍历所有员工,把所有员工的薪水,提升20%
for i in clerks.keys():
    clerks[i]['sal'] += clerks[i]['sal'] * 0.2
print(clerks)

# 6、按照员工号为？？的信息如下 年龄：？？名字：？？入职时间：？？薪水：？？的格式输出员工信息
for i in clerks.keys():
    clerk_info = clerks[i]
    print(f"员工号为{i}的信息如下:\n"
          f"年龄:{clerk_info['age']}\n"
          f"名字:{clerk_info['name']}\n"
          f"入职时间:{clerk_info['entry_time']}\n"
          f"薪水:{clerk_info['sal']}\n")
```



## 七、小结

### 7.1 数据容器比较

|      比较项      |        列表(list)        |        元组(tuple)         | 字符串(str) |     集合(set)      |                       字典(dict)                       |
| :--------------: | :----------------------: | :------------------------: | :---------: | :----------------: | :----------------------------------------------------: |
| 是否支持多个元素 |            √             |             √              |      √      |         √          |                           √                            |
|     元素类型     |           任意           |            任意            | 只支持字符  |        任意        |           Key:通常是字符串或数字，Value:任意           |
| 是否支持元素重复 |            √             |             √              |      √      |         ×          |               Key不能重复，Value可以重复               |
|     是否有序     |            √             |             √              |      √      |         ×          | 3.6版本之前是无序的，3.6版本之后开始支持元素有序的功能 |
|   是否支持索引   |            √             |             √              |      √      |         ×          |                           ×                            |
| 可修改项/可变性  |            √             |             ×              |      ×      |         √          |                           √                            |
|     使用场景     | 可修改、可重复的多个数据 | 不可修改、可重复的多个数据 |   字符串    | 不可重复的多个数据 |              通过关键字查询对应数据的需求              |
|     定义符号     |            []            |             ()             |   “” / ‘’   |         {}         |                      {key:value}                       |



### 7.2 数据容器小结

#### 7.2.1 通用序列操作

> 大多数序列类型，包括可变类型和不可变类型都支持下表中的操作

| 运算               | 结果                                                         |
| :----------------- | ------------------------------------------------------------ |
| x in s             | 如果 s 中的某项等于 x 则结果为***True***，否则为***False***. |
| x not in s         | 如果 s 中的某项等于 x 则结果为***False***，否则为***True***. |
| s + t              | s 与 t 相拼接.                                               |
| s * n 或 n * s     | 相当于 s 与自身进行 n 次拼接.                                |
| s[i]               | s 的第 i 项，起始为 0.                                       |
| s[i:j]             | s 从 i 到 j 的切片.                                          |
| s[i:j:k]           | s 从 i 到 j 步长为 k 的切片.                                 |
| len(s)             | s 的长度.                                                    |
| min(s)             | s 的最小项.                                                  |
| max(s)             | s 的最大项.                                                  |
| s.index(x[,i[,j]]) | x 在 s 中首次出现项的索引号(索引号在 i 或其后且在 j 之前).   |
| s.count(x)         | x 在 s 中出现的总次数.                                       |



#### 7.2.2 通用转换操作

| 序号 | 操作                                                         |
| :--: | ------------------------------------------------------------ |
|  1   | list([iterable]):<br />iterable 可以是序列、支持迭代的容器或其它可迭代对象,也就是`将指定的容器转成列表`. |
|  2   | str(容器):<br />将指定的容器转成字符串.                      |
|  3   | tuple([iterable]):<br />iterable 可以是序列、支持迭代的容器或其他可迭代对象,也就是将`指定的容器转成元组`. |
|  4   | set([iterable]):<br/>iterable 可以是序列、支持迭代的容器或其他可迭代对象,也就是`将指定的容器转成集合`. |

> 代码实现————数据容器转换

```python
str_a = "hello"
list_a = ['jack', 'tom', 'simon']
tuple_a = ('mary', 'ddd')
set_a = {'red', 'black'}
dict_a = {"001": "韩信", "002": "李白"}

# ① 将指定的容器转成列表list类型
print(f"str_a转换成list:{list(str_a)}")  # str_a转换成list:['h', 'e', 'l', 'l', 'o']
print(f"tuple_a转换成list:{list(tuple_a)}")  # tuple_a转换成list:['mary', 'ddd']
print(f"set_a转换成list:{list(set_a)}")  # set_a转换成list:['red', 'black']
print(f"dict_a转换成list:{list(dict_a)}")  # dict_a转换成list:['001', '002']

# ② 将指定的容器转成字符串str类型,注意:list_a转换为str后的结果相当于"['jack', 'tom', 'simon']",其余同理
print(f"list_a转换成str:{str(list_a)}")  # list_a转换成str:['jack', 'tom', 'simon']
print(f"tuple_a转换成str:{str(tuple_a)}")  # tuple_a转换成str:('mary', 'ddd')
print(f"set_a转换成str:{str(set_a)}")  # set_a转换成str:{'black', 'red'}
print(f"dict_a转换成str:{str(dict_a)}")  # dict_a转换成str:{'001': '韩信', '002': '李白'}

# ③ 将指定的容器转成元组tuple类型
print(f"str_a转换成tuple:{tuple(str_a)}")  # str_a转换成tuple:('h', 'e', 'l', 'l', 'o')
print(f"list_a转换成tuple:{tuple(list_a)}")  # list_a转换成tuple:('jack', 'tom', 'simon')
print(f"set_a转换成tuple:{tuple(set_a)}")  # set_a转换成tuple:('black', 'red')
print(f"dict_a转换成tuple:{tuple(dict_a)}")  # dict_a转换成tuple:('001', '002')

# ④ 将指定的容器转成集合set类型
print(f"str_a转换成set:{set(str_a)}")  # str_a转换成set:{'e', 'l', 'h', 'o'}
print(f"list_a转换成set:{set(list_a)}")  # list_a转换成set:{'jack', 'tom', 'simon'}
print(f"tuple_a转换成set:{set(tuple_a)}")  # tuple_a转换成set:{'mary', 'ddd'}
print(f"dict_a转换成set:{set(dict_a)}")  # dict_a转换成set:{'001', '002'}

# ⑤ 数据容器不能随意转成字典dict类型,否则会抛出ValueError异常
```



#### 7.2.3 其它操作说明

1. [列表的其它操作](https://docs.python.org/zh-cn/3.12/library/stdtypes.html#lists)
2. [元组的其它操作](https://docs.python.org/zh-cn/3.12/library/stdtypes.html#tuples)
3. [字符串的其它操作](https://docs.python.org/zh-cn/3.12/library/stdtypes.html#string-methods)
4. [集合的其它操作](https://docs.python.org/zh-cn/3.12/library/stdtypes.html#set)
5. [字典的其它操作](https://docs.python.org/zh-cn/3.12/library/stdtypes.html#dict)



### 7.3 传参机制

> 代码实现————列表list传参机制

```python
def f1(my_list):
    print(f"② f1() my_list:{my_list} 地址:{id(my_list)}")
    my_list[0] = "jack"
    print(f"③ f1() my_list:{my_list} 地址:{id(my_list)}")


# 测试
my_list = ["tom", "simon", "mary"]
print(f"① my_list:{my_list} 地址:{id(my_list)}")
f1(my_list)
print(f"④ my_list:{my_list} 地址:{id(my_list)}")

"""
列表list是可变的,但my_list[0] = "jack"改变的仅是my_list[0]的内存地址,my_list的地址并不会发生变化
Console Result:
① my_list:['tom', 'simon', 'mary'] 地址:2350379236096
② f1() my_list:['tom', 'simon', 'mary'] 地址:2350379236096
③ f1() my_list:['jack', 'simon', 'mary'] 地址:2350379236096
④ my_list:['jack', 'simon', 'mary'] 地址:2350379236096
"""
```

- 内存指向分析图

![image-20240310220142829](https://cdn.jsdelivr.net/gh/2329677402/img/img/202403102201963.png)



> 代码实现————元组tuple传参机制

```python
def f2(my_tuple):
    print(f"② f2() my_tuple:{my_tuple} 地址:{id(my_tuple)}")
    # 元组不可修改
    # my_tuple[0] = "red"  # 抛出TypeError异常
    print(f"③ f2() my_tuple:{my_tuple} 地址:{id(my_tuple)}")


# 测试
my_tuple = ("hi", "ok", "hello")
print(f"① my_tuple:{my_tuple} 地址:{id(my_tuple)}")
f2(my_tuple)
print(f"④ my_tuple:{my_tuple} 地址:{id(my_tuple)}")

"""
由于元组tuple的不可变性,它的内存地址始终不会发生变化
Console Result:
① my_tuple:('hi', 'ok', 'hello') 地址:1720925856640
② f2() my_tuple:('hi', 'ok', 'hello') 地址:1720925856640
③ f2() my_tuple:('hi', 'ok', 'hello') 地址:1720925856640
④ my_tuple:('hi', 'ok', 'hello') 地址:1720925856640
"""
```



> 代码实现————集合set传参机制

```python
def f3(my_set):
    print(f"② f3() my_set:{my_set} 地址:{id(my_set)}")
    my_set.add("红楼梦")
    print(f"③ f3() my_set:{my_set} 地址:{id(my_set)}")


# 测试
my_set = {"水浒传", "西游记", "三国演义"}
print(f"① my_set:{my_set} 地址:{id(my_set)}")
f3(my_set)
print(f"④ my_set:{my_set} 地址:{id(my_set)}")

"""
集合set的传参机制与列表list一致
Console Result:
① my_set:{'三国演义', '水浒传', '西游记'} 地址:2297253789280
② f3() my_set:{'三国演义', '水浒传', '西游记'} 地址:2297253789280
③ f3() my_set:{'红楼梦', '三国演义', '水浒传', '西游记'} 地址:2297253789280
④ my_set:{'红楼梦', '三国演义', '水浒传', '西游记'} 地址:2297253789280
"""
```



> 代码实现————字典dict传参机制

 ```python
def f4(my_dict):
    print(f"② f4() my_dict:{my_dict} 地址:{id(my_dict)}")
    my_dict['address'] = '西溪'
    print(f"③ f4() my_dict:{my_dict} 地址:{id(my_dict)}")


# 测试
my_dict = {"name": "Simon", "age": 21}
print(f"① my_dict:{my_dict} 地址:{id(my_dict)}")
f4(my_dict)
print(f"④ my_dict:{my_dict} 地址:{id(my_dict)}")

"""
字典dict的传参机制与列表list也是一致的
Console Result:
① my_dict:{'name': 'Simon', 'age': 21} 地址:1779077808064
② f4() my_dict:{'name': 'Simon', 'age': 21} 地址:1779077808064
③ f4() my_dict:{'name': 'Simon', 'age': 21, 'address': '西溪'} 地址:1779077808064
④ my_dict:{'name': 'Simon', 'age': 21, 'address': '西溪'} 地址:1779077808064
"""
 ```



### 7.4 数据类型

> `可变数据类型`:变量值改变，内存地址不变；`不可变数据类型`:变量值改变，内存地址也改变.

![image-20240310231048975](https://cdn.jsdelivr.net/gh/2329677402/img/img/202403102310248.png)







# :mag: ​排序和查找



## 一、排序

> 排序的介绍​​

- 排序是将多个数据，按照指定的顺序进行排列的过程
- 排序的分类
	1. `冒泡排序`
	2. 选择排序
	3. 插入排序
	4. 希尔排序
	5. 归并排序
	6. 快速排序
	7. 堆排序
	8. 计数排序
	9. 桶排序
	10. 基数排序



### 1.1 冒泡排序法

> 介绍

- 冒泡排序(Bubble Sorting)的基本思想是:

	重复地走访需要排序的元素列表，依次比较两个相邻的元素，如果顺序(如从大到小或从小到大)错误就交换它们的位置.重复地进行直到没有相邻的元素需要交换，则元素列表排序完成.

- 在冒泡排序中，值最大(或最小)的元素会通过交换慢慢"浮"到元素列表的"顶端”.就像"冒泡"一样，所以被称为冒泡排序.

> 代码演示————列表:[24, 69, 80, 57, 13]有5个元素，要求
>
> 使用冒泡排序法将其排成一个从小到大的有序列表.

![image-20240312212354652](https://cdn.jsdelivr.net/gh/2329677402/img/img/202403122123039.png)

```py
# 定义列表
num_list = [24, 69, 80, 57, 13]
# center方法传入的两个参数:字符串总长度, 字符串两边填充的符号
print("排序前".center(32, "-"))
print(f"num_list:{num_list}")

"""
# 使用sort方法完成排序
num_list.sort()
print("排序后".center(32, "-"))
print(f"num_list:{num_list}")

# --------------排序后---------------
# num_list:[13, 24, 57, 69, 80]
"""


# 冒泡排序
def bubble_sort(my_list):
    """
    功能:对传入的列表排序——从小到大.
    :param my_list: 传入的列表
    :return: 无
    """
    # 第一轮排序:把最大的数放到最后的位置
    # j 控制当前比较次数,同时可以作为比较元素的索引下标
    for j in range(0, 4):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    print("第一轮排序结果:", my_list)

    # 第二轮排序:把第二大数放到倒数第二的位置
    # j 控制当前比较次数,同时可以作为比较元素的索引下标
    for j in range(0, 3):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    print("第二轮排序结果:", my_list)

    # 第三轮排序:把第三大数放到倒数第三的位置
    # j 控制当前比较次数,同时可以作为比较元素的索引下标
    for j in range(0, 2):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    print("第三轮排序结果:", my_list)

    # 第四 轮排序:把第四大数放到倒数第四的位置
    # j 控制当前比较次数,同时可以作为比较元素的索引下标
    for j in range(0, 1):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    print("第四轮排序结果:", my_list)


bubble_sort(num_list)
"""
第一轮排序结果: [24, 69, 57, 13, 80]
第二轮排序结果: [24, 57, 13, 69, 80]
第三轮排序结果: [24, 13, 57, 69, 80]
第四轮排序结果: [13, 24, 57, 69, 80]
"""

# 将以上写死的数据替换为可接收的参数
# 从控制台中接收一组以空格分隔的数字
user_input = input("请输入一组以空格分隔的数字: ")

# 使用列表生成式将输入的字符串以空格分割成单独的数字，并将其转换为int类型并添加到列表中
num_list = [int(i) for i in user_input.split()]


def user_sort(my_list):
    # i 控制第几轮排序
    for i in range(0, len(my_list) - 1):
        # j 控制当前比较次数
        for j in range(0, len(my_list) - 1 - i):
            # 如果前者大于后者,则互换元素值
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
        print(f"第{i + 1}轮排序结果:", my_list)


user_sort(num_list)
"""
请输入一组以空格分隔的数字: 67 23 98 30 25 10
第1轮排序结果: [23, 67, 30, 25, 10, 98]
第2轮排序结果: [23, 30, 25, 10, 67, 98]
第3轮排序结果: [23, 25, 10, 30, 67, 98]
第4轮排序结果: [23, 10, 25, 30, 67, 98]
第5轮排序结果: [10, 23, 25, 30, 67, 98]
"""
```



## 二、查找

> 查找的介绍

1. `顺序查找`
2. `二分查找`
3. 插值查找
4. 斐波那契查找
5. 树表查找
6. 分块查找
7. 哈希查找



### 2.1 顺序查找

> 代码演示————有一个列表:names_list = ["李白", "韩信", "百里玄策", "东方镜"]，要求
>
> 从键盘中任意输入一个名称，判断列表中是否包含此名称，如果找到就提示，并给出下标值.

```py
names_list = ["李白", "韩信", "百里玄策", "东方镜"]
find_name = "韩信"


# 使用index方法完成查找,但是未找到指定元素会抛出ValueError异常
# res_index = names_list.index(find_name)
# print("res_index:", res_index)

def seq_search(my_list, find_val):
    """
    功能:顺序查找指定的元素.
    :param my_list: 传入的列表.
    :param find_val: 要查找的值/元素.
    :return: 如果查找到则返回对应的索引下标,否则返回None.
    """
    # 初始化需要查找元素的索引下标.
    find_index = None
    for i in range(len(my_list)):
        # 开始比较,如果匹配上,返回索引
        if my_list[i] == find_val:
            print(f"{find_val}对应的索引下标是:{i}.")
            find_index = i
            break
    else:
        print(f"没有找到{find_val}")
    return find_index


res_index = seq_search(names_list, find_name)  # 韩信对应的索引下标是:1.
print("res_index:", res_index)  # res_index: 1

"""
拓展:如果一个列表中有多个要查找的元素/值,如何将满足的元素下标都返回.
"""
names_list2 = ["李白", "韩信", "百里玄策", "韩信", "东方镜"]
find_name2 = "韩信"


def seq_search2(my_list, find_val):
    """
    功能:顺序查找指定的元素.
    :param my_list: 传入的列表.
    :param find_val: 要查找的值/元素.
    :return: 如果查找到则将对应的索引下标追加到空列表find_index中,否则返回空列表[].
    """
    # 定义空列表
    find_index = []
    for i in range(len(my_list)):
        # 开始比较,如果匹配上则将对应的索引下标追加到空列表find_index中
        if my_list[i] == find_val:
            find_index.append(i)
    print(f"{find_val}对应的索引下标是:{find_index}.")
    return find_index


res_index2 = seq_search2(names_list2, find_name2)  # 韩信对应的索引下标是:[1, 3].
print("res_index2:", res_index2)  # res_index2: [1, 3]
```



### 2.2 二分查找

> 代码演示————请对一个列表(元素从小到大排序的)进行二分查找[1, 8, 10, 89, 1000, 1234],输入一个数看看该列表是否存在此数，并且求出下标，如果没有，返回-1.

1. 二分查找的前提是该列表已经是一个排好序的列表.
2. 排列的顺序从小到大或从大到小会影响二分查找的逻辑.

```py
"""
思路分析:
1.找到列表的中间数 mid_val 和 find_val 比较;
2.如果mid_val > find_val ,则到 mid_val的左边查找;
3.如果mid_val < find_val ,则到 mid_val的右边查找;
4.如果mid val = find val ,返回对应的下标即可;
5.不断的重复 步骤1-4,这里就是不断的折半,使用while;
6.如果while 结束,都没有找到,说明find_val 没有在列表中.
"""
num_list = [1, 8, 10, 89, 1000, 1234]


# 编写二分查找函数(列表从小到大)
def binary_search(my_list, find_val):
    """
    功能:完成二分查找.
    :param my_list: 要查找的列表(从小到大).
    :param find_val: 要查找的元素.
    :return: 如果找到返回对应的下标,如果没找到,返回-1.
    """
    # 初始化最左/右边的索引下标
    left_index, right_index = 0, len(my_list) - 1
    # 定义需要查找元素的下标
    find_index = -1
    # 使用while循环,不断折半比较中间值,比较的前提是满足:left_index <= right_index.
    while left_index <= right_index:
        # 定义中间数的索引
        mid_index = (left_index + right_index) // 2

        # 如果mid_val > find_val,则到mid_val左边查找(列表从小到大).
        if my_list[mid_index] > find_val:
            right_index = mid_index - 1

        # 如果mid_val < find_val,则到mid_val右边查找(列表从小到大).
        elif my_list[mid_index] < find_val:
            left_index = mid_index + 1

        # mid_val = find_val,找到
        else:
            find_index = mid_index
            break
    else:
        print("未找到")
    return find_index


res_index = binary_search(num_list, 1234)
print("res_index:", res_index)  # res_index: 5
```



## 三、小结

> 1. 代码实现————随机生成10个整数(1-100)保存到列表中，使用冒泡排序，对其从大到小排序.
> 2. 代码实现————在前题的基础上，使用二分查找，查找是否有8这个数，如果有，返回对应的下标，否则返回-1.

```py
# 1、随机生成10个整数(1-100)保存到列表中，使用冒泡排序，对其从大到小排序.
import random

num_list = []
# 生成随机列表
for i in range(10):
    num_list.append(random.randint(1, 100))
print("随机生成的列表为:", num_list)


# 冒泡排序
def bubble_sort(my_list):
    """
    :param my_list: 要排序的列表(从大到小).
    :return: 无
    """
    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - 1 - i):
            if my_list[j] < my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
        print(f"第{i + 1}轮排序结果:", my_list)


bubble_sort(num_list)


# 2、使用二分查找，查找是否有8这个数，如果有，返回对应的下标，否则返回-1.
# 二分查找
def binary_search(my_list, find_val):
    """
    :param my_list: 要查找的列表(从大到小).
    :param find_val: 要查找的元素.
    :return: 如果找到返回对应的下标,如果没找到,返回-1.
    """
    # 初始化最左/右边的索引下标
    left_index, right_index = 0, len(my_list) - 1
    # 定义需要查找元素的下标
    find_index = -1
    # 使用while循环,不断折半比较中间值,比较的前提是满足:left_index <= right_index.
    while left_index <= right_index:
        # 定义中间数的索引
        mid_index = (left_index + right_index) // 2

        if my_list[mid_index] < find_val:
            right_index = mid_index - 1

        elif my_list[mid_index] > find_val:
            left_index = mid_index + 1

        else:
            find_index = mid_index
            break
    else:
        print(f"未在列表中找到{find_val}！")
    return find_index


res_index = binary_search(num_list, 8)
print("res_index:", res_index)

"""
Console Result：
随机生成的列表为: [40, 90, 89, 71, 57, 4, 45, 8, 87, 3]
第1轮排序结果: [90, 89, 71, 57, 40, 45, 8, 87, 4, 3]
第2轮排序结果: [90, 89, 71, 57, 45, 40, 87, 8, 4, 3]
第3轮排序结果: [90, 89, 71, 57, 45, 87, 40, 8, 4, 3]
第4轮排序结果: [90, 89, 71, 57, 87, 45, 40, 8, 4, 3]
第5轮排序结果: [90, 89, 71, 87, 57, 45, 40, 8, 4, 3]
第6轮排序结果: [90, 89, 87, 71, 57, 45, 40, 8, 4, 3]
第7轮排序结果: [90, 89, 87, 71, 57, 45, 40, 8, 4, 3]
第8轮排序结果: [90, 89, 87, 71, 57, 45, 40, 8, 4, 3]
第9轮排序结果: [90, 89, 87, 71, 57, 45, 40, 8, 4, 3]
res_index: 7
"""
```







# :bug: ​断点调试(Debug)​

## 一、断点调试介绍
