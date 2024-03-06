"""
集合常用操作

- 函数
    1、len(set):获取个数

- 方法
    1、x in s:检测元素x是否为集合s中的成员
    2、set.add(i):将元素i添加到集合中
    3、set.remove(i):移除元素i,如果不存在则抛出KeyError异常
    4、set.pop():移除并返回任意一个元素,如果为空抛出KeyError异常
    5、set.clear():移除所有元素
    6、union(*others) set|other|...:返回一个新集合,其中包含来自原集合以及others指定的所有集合中的元素
    7、intersection(*others) set & other & ...:返回一个新集合,其中包含来自原集合以及others指定的所有集合中共有的元素
    8、difference(*others) set - other - ...:返回一个新集合,其中包含来自原集合以及others指定的其它集合中不存在的元素
"""
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

apps = {'WeChat', 'Telegram', 'Twitter'}
apps2 = {'Twitter', 'Facebook', 'Telegram', 'TikTok'}
# union,相当于数学中的合集(并集),即:将集合A和B合并并组成新的集合
# 等价于apps3 = apps.union(apps2)
apps3 = apps | apps2
print(apps3)  # {'Twitter', 'WeChat', 'Facebook', 'TikTok', 'Telegram'}

# intersection,相当于数学中的交集,即:将集合A和B共有的元素取出并组成新的集合
# 等价于apps4 = apps.intersection(apps2)
apps4 = apps & apps2
print(apps4)  # {'Twitter', 'Telegram'}

# difference,相当于数学中的差集,即:将只存在于集合A中的元素取出并组成新的集合
# 等价于apps5 = apps.difference(apps2)
apps5 = apps - apps2
print(apps5)  # {'WeChat'}
