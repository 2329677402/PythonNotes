"""
一个公司有多个员工，请使用合适的数据类型保存员工的信息(比如员工号、年龄、名字、入职时间、薪水等)，要求
1)员工号是入职时分配的，唯一不重复
2)通过员工号，可以查询到员工的信息
3)根据需要，可以动态的增加、删除员工
4)根据需要，可以修改员工的信息(比如 年龄、名字、入职时间、薪水等)

像这种基于Key 查询Value 的场景需求,是一种映射关系.而列表,元组,集合都是一种单值存储,处理映射关系并不方便,由此便引入了字典dict

- 基本介绍
    1、字典(dict, 全称dictionary)是一种常用的Python数据类型,在其他语言中可能把字典称为联合内存或联合数组
    2、字典是一种映射类型,专门处理通过key查询Value的需求

- 字典的定义
    创建一个字典,只要用逗号分隔的不同的元素,并用{}括起来即可,存储的元素称为键值对,如:
    dict_a = {key:value, key:value, key:value}
    通过key取出对应的value: 字典名[key]

- 注意事项和细节
    1、字典的Key通常是字符串或数字,Value可以是任何数据类型
    2、字典不支持索引,否则会抛出KeyError异常
    3、既然字典不支持索引,所以对字典进行遍历不支持while,只支持for
        注:对字典进行遍历,遍历的对象是Key,而不是Key:Value
    4、创建空字典:dict_test = {} 或 dict_test = dict()
    5、字典的Key必须是唯一的,如果指定了多个相同的Key,后面的键值对会覆盖前面的
"""
# 定义字典
dict_a = {'book': '编程', 'name': 'Python', 'price': 99.8}
print(type(dict_a))  # <class 'dict'>
print(dict_a['name'])  # Python

# 注意事项3
dict_b = {'a': 1, 'b': 2, 'c': 3}
# 获取value的3种方法
print('-------遍历方式①-------')
for i in dict_b:
    print(f'key:{i},value:{dict_b[i]}')

print('-------遍历方式②-------')
for i in dict_b.values():
    print(f'value:{i}')

print('-------遍历方式③-------')
for i, j in dict_b.items():
    print(f'key:{i},value:{j}')

# 注意事项5
dict_c = {'a': 1, 'b': 2, 'c': 3, 'b': 200}
print(dict_c)  # {'a': 1, 'b': 200, 'c': 3}
