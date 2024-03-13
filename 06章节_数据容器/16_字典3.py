"""
练习题:员工信息管理问题

一个公司有多个员工，请使用合适的数据类型保存员工的信息(比如员工号、年龄、名字、入职时间、薪水等)，要求
1)员工号是入职时分配的，唯一不重复
2)通过员工号(0010)，可以查询到员工的信息
3)根据需要，可以动态的增加、删除员工
4)根据需要，可以修改员工的信息(比如 年龄、名字、入职时间、薪水等)
"""
# 1、员工号是入职时分配的，唯一不重复
clerks = {
    '0001': {
        "age": 20,
        "name": "贾宝玉",
        "entry_time": "2011-11-11",
        "sal": 12000
    },
    '0002': {
        "age": 21,
        "name": "薛宝钗",
        "entry_time": "2015-12-12",
        "sal": 10000
    },
    '0010': {
        "age": 18,
        "name": "林黛玉",
        "entry_time": "2018-10-10",
        "sal": 20000
    }
}

# 2、通过员工号(0010)，可以查询到员工的信息
msg_0010 = clerks['0010']
print(
    f"员工号0010的员工信息:\n年龄:{msg_0010['age']}\n姓名:{msg_0010['name']}\n入职时间:{msg_0010['entry_time']}\n工资:{msg_0010['sal']}")

"""
Console Result:
员工号0010的员工信息:
年龄:18
姓名:林黛玉
入职时间:2018-10-10
工资:20000
"""

# 3、根据需要，可以动态的增加、删除员工
clerks['0020'] = {
    "age": 22,
    "name": "韩信",
    "entry_time": "2024-03-15",
    "sal": 50000
}
print(clerks)
del clerks['0002']
print(clerks)

# 4、根据需要，可以修改员工的信息(比如 年龄、名字、入职时间、薪水等)
# 方式①
clerks['0001'] = {
    "age": 25,
    "name": "宝玉",
    "entry_time": "2021-10-01",
    "sal": 22000
}
print(clerks)
# 方式②
clerks['0001']['age'] = 27
clerks['0001']['entry_time'] = "2023-10-01"
clerks['0001']['sal'] += clerks['0001']['sal'] * 0.1
print(clerks)

# 5、遍历所有员工,把所有员工的薪水,提升20%
for i in clerks.keys():
    clerks[i]['sal'] += clerks[i]['sal'] * 0.2
print(clerks)

# 6、按照员工号为？？的信息如下 年龄：？？名字：？？入职时间：？？薪水：？？的格式输出员工信息
for i in clerks.keys():
    clerk_info = clerks[i]
    print(f"员工号为{i}的信息如下:\n"
          f"年龄:{clerk_info['age']}\n"
          f"名字:{clerk_info['name']}\n"
          f"入职时间:{clerk_info['entry_time']}\n"
          f"薪水:{clerk_info['sal']}\n")