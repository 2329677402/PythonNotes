"""
- 基本介绍
    1、在Python中处理文本数据是使用str对象,也称为字符串.字符串是由Unicode编码构成的不可变序列.
        Unicode码是一种字符编码,相应的还有utf-8,,gbk等
        ord()函数 用于返回单个字符对应的unicode编码值

    2、字符串字面值的三种写法
        单引号:'可以嵌入"双引号"'
        双引号:"可以嵌入'单引号'"
        三重引号:三重单引号,三重双引号

    3、字符串是字符的容器,一个字符串可以存放多个字符

- 字符串支持索引
    使用:
        字符串名[索引]
    例如:
        str1 = "red - green"
        print(str1[4])  # -

- 字符串的遍历(用法与列表一致)
    将字符串的每个元素依次取出，进行处理的操作，就是遍历/迭代

- 注意事项和细节
    1、字符串索引必须在指定范围内使用，否则报：IndexError:tuple index out of range (与列表、元组特性一致)
    2、字符串是不可变序列,不可修改 (与元组特性一致)

字符串常用操作
- 函数
    1、len(str)

- 方法
    1、str.replace(old, new[,count]):返回字符串的副本,其中出现的所有子字符串old替换为new,可选参数count:替换前count个
    2、str.split(sep = None, maxsplit = -1):返回一个有字符串内单词组成的列表,使用sep作为分隔字符串.如果给出了 maxsplit，
        则最多进行 maxsplit 次拆分（因此，列表最多会有 maxsplit+1 个元素）.如果 maxsplit 未指定或为 -1，则不限制拆分次数（进行所有可能的拆分）.
    3、str.count(sub):统计指定字符串在字符串中出现的次数
    4、str.index(sub):从字符串中找出指定字符串第一个匹配项的索引值
    5、str.strip([chars]):返回原字符串的副本，移除其中的前导和末尾字符。 chars参数为指定要移除字符的字符串.
        一般用于去除前后空格或指定字符串
    6、str.lower():返回原字符串小写的副本
    7、str.upper():返回原字符串大写的副本
"""

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
