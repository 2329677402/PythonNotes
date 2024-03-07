"""
列表的注意事项和使用细节
"""

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
print(list6[2], id(list6[2]))  # 2248170988080
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
