"""
- 基本介绍
    1、切片:从一个序列中,取出一个子序列
    2、序列:内容连续、有序,可使用索引的一类数据容器
    3、列表(list)、元组(tuple)、字符串均可视为序列

- 基本语法
    序列[起始索引:结束索引:步长]
    1、表示从序列中,从指定的起始索引开始,按照指定的步长,依次取出元素,到指定结束索引为止,截取到一个新的序列
    2、切片操作是 前闭后开 ,即[起始索引:结束索引)
    3、步长表示:依次取出元素的间隔
        步长为1:每次跳过0个元素取值,即:每个元素都取出.同时也是默认值
        步长为2:每次跳过1个元素取值
        步长为N:每次跳过N-1个元素取值
"""
# 注意:切片当中的符号是冒号: 而不是逗号,
str1 = "hello,world"

# 截取hello
str_slice = str1[0:5]
print(str_slice)  # hello

list1 = ["hello", "jack", "tom", "simon"]
# 截取["jack", "simon"]
list_slice = list1[1:4:2]
print(list_slice)  # ['jack', 'simon']

tuple1 = (100, 300, 700, 1000, 3000)
# 截取(300, 700, 1000, 3000)
tuple_slice = tuple1[1:5]
print(tuple_slice)  # (300, 700, 1000, 3000)

"""
- 注意事项和使用细节
    序列[起始索引:结束索引:步长]
    1、起始索引默认从0开始,结束索引默认截取到结尾,步长默认为1
    2、步长为负时,表示反向取值,同时起始索引和结束索引的默认值也变为了-1和-总长
    3、切片操作并不会影响原序列,而是返回了一个新序列        
"""
str2 = "hello,world"

# 注意事项①
str2_a = str2[:5:1]
print(str2_a)  # hello

str2_b = str2[1::1]
print(str2_b)  # ello,world

str2_c = str2[::2]
print(str2_c)  # hlowrd

str2_d = str2[2:7:]
print(str2_d)  # llo,w

# 注意事项②
str2_e = str2[::-1]
print(str2_e)  # dlrow,olleh

str2_f = str2[-1:-6:-1]
print(str2_f)  # dlrow

print("---" * 20)
content = """
定义列表list_name = ["Jack", "Lisa","Hsp","Paul","Simon","Kobe"]
- 取出前三个名字
- 取出后三个名字,并且保证原来的顺序
"""
print(f"demo:{content}")

list_name = ["Jack", "Lisa", "Hsp", "Paul", "Simon", "Kobe"]

# 问题1
list1 = list_name[:3:]
print(list1)  # ['Jack', 'Lisa', 'Hsp']

# 问题2
list2 = list_name[:-4:-1]
print(list2)  # ['Kobe', 'Simon', 'Paul']
# ① 使用reverse反转列表元素
list2.reverse()
print(list2)  # ['Paul', 'Simon', 'Kobe']
# ② 使用切片再次倒序
list3 = list2[::-1]
print(list3)  # ['Paul', 'Simon', 'Kobe']
