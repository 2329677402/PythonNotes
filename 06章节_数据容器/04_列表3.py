"""
列表的常用操作

- 函数
    1、len(list):返回列表元素个数
    2、max(list):返回列表元素最大值
    3、min(list):返回列表元素最小值
    4、list(tuple):将元组转换为列表

- 方法
    1、list.append(obj):在列表末尾添加新的对象
    2、list.count(obj):统计某个元素在列表中出现的次数
    3、list.extend(seq):在列表末尾一次性追加另一个序列中的多个值(用新列表扩展原列表)
    4、list.index(obj):从列表中找出某个值第一个匹配项的索引值
    5、list.insert(index, obj):将对象插入列表
    6、list.pop([index = -1]):移除列表中的一个元素(默认最后一个元素),并且返回该元素的值
    7、list.remove(obj):移除列表中某个值的第一个匹配项
    8、list.reverse():反转列表元素
    9、list.sort(key = None, reverse = False):对原列表进行排序
    10、list.clear():清空列表
    11、list.copy():复制列表
"""

# demo
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

"""
列表生成式
    1、列表生成式就是"生成列表的公式"
    2、基本语法
        [列表元素的表达式 for 自定义变量 in 可迭代对象]
        如:[i * 2 for i in range(1, 5)] -> 得到列表[2, 4, 6, 8]
        list = [i + i for i in "Simon"] -> 得到列表['SS', 'ii', 'mm', 'oo', 'nn']
"""

print("---" * 20)
content = "生成一个列表，内容为[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"
print(f"demo:{content}")
list1 = [i ** 2 for i in range(1, 11)]
print(list1)

print("---" * 20)
content2 = "循环从键盘输入5个成绩，保存列表并输出"
print(f"demo2:{content2}")
list_score = []
for i in range(5):
    score = float(input(f"请输入第{i + 1}个成绩:"))
    list_score.append(score)
print("5个学生的成绩为:", list_score)
