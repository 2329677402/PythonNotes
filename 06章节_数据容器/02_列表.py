"""
- 基本介绍
    1、列表可以存放多个不同类型数据，即：列表就是一列数据(多个数据)
    2、列表也是一种数据类型

- 列表的定义
    创建一个列表，只要用逗号分隔的不同的数据项使用方括号括起来即可:
    list1 = [100, 200, 300, 400, 500]
    list2 = ['red', 'green', 'blue', 'yellow', 'white', 'black']

- 列表的使用
    列表名[索引]

- 列表的遍历
    将列表的每个元素依次取出，进行处理的操作，就是遍历/迭代
"""

# 定义列表
list1 = [100, 200, 300, 400, 500]

# 使用列表
print(list1)  # [100, 200, 300, 400, 500]
print(type(list1))  # <class 'list'>
print(list1[0])  # 100
print(list1[4])  # 500
# print(list1[5])  # IndexError


# Python内置函数len():返回对象的长度(元素个数)
print(len(list1))  # 5

# while遍历列表
index = 0
while index < len(list1):
    print(f"第{index + 1}个元素是:{list1[index]}")
    index += 1

# for遍历列表
for i in list1:
    print(i)

print("-----使用列表解决养鸡场问题-----")
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
