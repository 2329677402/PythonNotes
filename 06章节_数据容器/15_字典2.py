"""
字典常用操作
    1、len(dict):返回字典的键值对个数
    2、d[key]:返回字典d中以key为键的value值,如果key值不存在则抛出KeyError异常
    3、d[key] = value:如果key值存在,修改原value值;反之,则是增加一个key-value键值对
    4、del d[key]:如果key值存在,移除该键值对;反之抛出异常
    5、pop(key[,default]):如果key值存在,移除该键值对并返回value值;否则返回default;如果不给default且key值不存在,抛出异常
    6、keys():返回字典中所有的key值
    7、key in d:如果字典d中存在key值,返回True;否则返回False
    8、clear():移除字典中所有的键值对
"""
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

"""
字典生成式
    1、需求如下:
    给出了如下两个列表:
        books = ["红楼梦", "三国演义", "西游记", "水浒传"]
        authors = ["曹雪芹", "罗贯中", "吴承恩", "施耐庵"]
    生成对应的字典:
        {'红楼梦': '曹雪芹', '三国演义': '罗贯中', '西游记': '吴承恩', '水浒传': '施耐庵'}
    
    2、内置函数zip()
    作用:zip()可以将可迭代的对象作为参数,将对象中对应的元素打包成一个元组,返回由这些元组组成的列表
    字典生成式基本语法:
        {字典key的表达式:字典value的表达式 for 表示key的变量,表示value的变量 in zip(可迭代对象,可迭代对象)}
"""

# demo1
books = ["红楼梦", "三国演义", "西游记", "水浒传"]
authors = ["曹雪芹", "罗贯中", "吴承恩", "施耐庵"]

dict_b = {i: j for i, j in zip(books, authors)}
print(dict_b)  # {'红楼梦': '曹雪芹', '三国演义': '罗贯中', '西游记': '吴承恩', '水浒传': '施耐庵'}

# demo2
str1 = 'Simon'
dict_c = {i: j * 2 for i, j in zip(str1, str1)}
print(dict_c)  # {'S': 'SS', 'i': 'ii', 'm': 'mm', 'o': 'oo', 'n': 'nn'}

"""
demo3
给出两个列表:
english_list = ["red", "black", "yellow", "white"]
chinese_list = ["红色", "黑色", "黄色", "白色"]
生成一个字典:
{'红色': 'RED', '黑色': 'BLACK', '黄色': 'YELLOW', '白色': 'WHITE'}
"""
english_list = ["red", "black", "yellow", "white"]
chinese_list = ["红色", "黑色", "黄色", "白色"]
dict_d = {i: j.upper() for i, j in zip(chinese_list, english_list)}
print(dict_d)  # {'红色': 'RED', '黑色': 'BLACK', '黄色': 'YELLOW', '白色': 'WHITE'}
