"""
for循环、 while循环
"""

"""
① for循环基本语法
for <变量> in <范围/序列>:
    <循环操作语句>
    
- 说明
1、for、in是关键字，是规定好的
2、<范围/序列>可以理解为要处理的数据集，需要是可迭代对象（比如字符串、列表等）
3、循环操作语句，这里可以有多条语句，也就是要循环执行的代码，也叫循环体
4、Python的for循环是一种“轮询机制”，是对指定的数据集，进行“轮询处理”
"""
print("---" * 20)
content1 = "编写一个程序，可以打印10句“Hello World！”。"
print(f"demo1:{content1}")
"""
range函数详解
class range(stop)
class range(start, stop, step = 1)
1、虽然被称为函数，但range实际上是一个不可变的序列类型
2、range默认增加的步长step为1，也可以指定，start默认是0
3、通过list()可以查看range()生成的序列包含的数据
    i1 = range(10)
    print(list(i1))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    i2 = range(1, 10, 2)
    print(list(i2))  # [1, 3, 5, 7, 9]
4、range()生成的数列是前闭后开(左包含右不包含)
"""
for i in range(10):
    print(f"第{i + 1}句：Hello World!")

"""
for可以和else配合使用
- 语法格式
for <变量> in <序列>:
    <循环体>
else:
    <其它语句> 
else语句执行条件：for语句全部迭代完成
注意：如果for循环体中遇到break等中断循环，不会执行else语句
"""
print("---" * 20)
for i in range(3):
    print(f"第{i + 1}次：hello")
    # break中断
    # if i == 2:
    #     break
else:
    print("for循环迭代完毕！")

"""
② while循环基本语法
while 判断条件:
    <循环操作语句>

- 说明
1、while是关键字，是规定好的
2、当判断条件为True时，就执行循环操作语句，如果为False，就退出while
3、循环操作语句，这里可以有多条语句，也就是要循环执行的代码，也叫循环体
"""
print("---" * 20)
content2 = "编写一个程序，使用while打印10句“Hello World！”。"
print(f"demo2:{content2}")
i = 1
while i <= 10:
    print(f"第{i}句：Hello World!")
    i += 1
print("终止循环")

"""
while可以和else配合使用
- 语法格式
while 判断条件:
    <循环体>
else:
    <其它语句> 
else语句执行条件：while的判断条件为False时执行else语句
注意：如果while循环体中遇到break等中断循环，不会执行else语句
"""
print("---" * 20)
i = 1
while i <= 3:
    print(f"第{i}句：Hello World!")
    i += 1
    # break中断
    # if i == 3:
    #     break
else:
    print("while判断条件已为False！")

# 循环控制练习题
print("---" * 20)
content3 = "打印1-100之间所有能被3整除的数"
print(f"demo3:{content3}")
i = 1
count = 0
while i <= 100:
    if i % 3 == 0:
        print(i)
        count += 1
    i += 1
else:
    print(f"打印完毕！1-100之间有{count}个能被3整除的数")

print("---" * 20)
content4 = "打印40-200之间所有的偶数"
print(f"demo4:{content4}")
i = 40
count = 0
while i <= 200:
    if i % 2 == 0:
        print(i)
        count += 1
    i += 1
else:
    print(f"打印完毕！40-200之间有{count}个偶数")

print("---" * 20)
content5 = "不断输入姓名，直到输入“exit”为止"
print(f"demo5:{content5}")
name = ""
while name != "exit":
    name = input("请输入你的姓名：")
print("输入exit，终止循环！")

print("---" * 20)
content6 = "打印1~100之间所有是9的倍数的整数，统计个数及总和"
print(f"demo6:{content6}")
i = 1
sum = 0
count = 0
while i <= 100:
    if i % 9 == 0:
        print(i)
        sum += i
        count += 1
    i += 1
else:
    print(f"打印完毕！1~100之间所有是9的倍数的整数，个数是{count}，总和是{sum}")

print("---" * 20)
content7 = """
需求是输入一个整数，输出所有两个不大于这个数的整数之和等于该整数的公式，如：
请输入一个整数6
0 + 6 = 6
1 + 5 = 6
2 + 4 = 6
3 + 3 = 6
4 + 2 = 6
5 + 1 = 6
6 + 0 = 6
"""
print(f"demo7:{content7}")
number = int(input("请输入一个整数："))
i = 0
j = number
while i <= number:
    print(f"{i} + {j} = {number}")
    i += 1
    j -= 1
print("输出完毕！")
