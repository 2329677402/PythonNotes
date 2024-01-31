# demo：从控制台接受用户信息,[姓名，年龄，成绩]

name = input("请输入姓名：")
age = input("请输入年龄：")
score = input("请输入成绩：")

print("\n输入的信息如下：")
print(name)
print(age)
print(score)

# 注意：从控制台接收到的数据都为str类型
print(type(age))  # <class 'str'>
print(type(score))  # <class 'str'>

# 如果需要对接收到的数据进行算术运算，则需要进行类型转换
print(10 + float(score))

# 也可以在接收数据的时候，直接转成需要的类型
age = int(input("\n请输入年龄："))
print("age的数据类型是：", type(age))
