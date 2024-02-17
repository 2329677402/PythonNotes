import random

print("---" * 20)
content1 = """
需求：
① 随机生成1-100的一个数，直到生成了97这个数，退出循环并求出生成次数
② 提示：使用random模块的randint()函数来生成随机数，该函数语法为
    random.randint(a, b)
    作用：返回随机整数N满足a <= N <=b.相当于randrange(a, b+1).
"""
print(f"demo1:{content1}")
count = 0
while True:
    i = random.randint(1, 100)
    print(f"第{count + 1}次：{i}")
    count += 1
    if i == 97:
        break
print(f"总共生成了{count}次")

"""
注意事项和细节说明
1、break语句是用在for或while循环所嵌套的代码
2、它会中断最近的外层循环，如果循环有可选的else子句，也会跳过该子句
    count = 0
    while True:
        print("Hi while")
        count += 1
        if count == 3:
            break
        while True:
            print("OK while")
            break
    else:
        print("Hello,while")
    # Hi while
    # OK while
    # Hi while
    # OK while
    # Hi while
3、如果一个for循环被break所终结，该循环的控制变量会保持其当前值
    nums = [1, 2, 3, 4, 5, 6]
    for i in nums:
        if i > 3:
            break
    print("i =", i)
    # i= 4
"""

print("---" * 20)
content2 = "1-100以内的数求和，求出当和第一次大于20时的当前控制循环的变量值是多少？"
print(f"demo2:{content2}")
sum = 0
for i in range(1, 101):
    sum += i
    if sum > 20:
        break
print("i =", i)

print("---" * 20)
content3 = "实现登录验证，有三次机会，如果用户名为‘张无忌’，密码为‘888’，提示登录成功，否则提示还有几次机会，使用for+break完成"
print(f"demo3:{content3}")
for i in range(1, 4):
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == "张无忌" and password == "888":
        print("登录成功")
        break
    else:
        print(f"还有{3 - i}次机会")
