"""
元组的注意事项和使用细节
"""
# 1、如果我们需要一个空元组，可以通过tuple_test = ()，或者tuple_test = tuple()方式来定义 (与列表类似)

# 2、元组的元素可以有多个，而且数据类型没有限制，允许有重复元素，并且是有序的 (与列表类似)

# 3、元组的索引/下标是从0开始的 (与列表类似)

# 4、元组索引必须在指定范围内使用，否则报：IndexError:tuple index out of range (与列表类似)

# 5、索引也可以从尾部开始，最后一个元素的索引为-1，往前一位为-2，以此类推 (与列表类似)

# 6、元组是不可变序列 (区别与列表是可变序列)
tuple1 = (1, 2, 3)
# tuple1[0] = 100  # TypeError
print(tuple1)

# 7、但是可以修改元组内list的内容(增删改均可)
tuple2 = (1, 3, [5, 7, "张飞"], "牛魔")
print(tuple2)  # (1, 3, [5, 7, '张飞'], '牛魔')
# 修改
tuple2[2][1] = "李信"
print(tuple2)  # (1, 3, [5, '李信', '张飞'], '牛魔')
# 删除
del tuple2[2][0]
print(tuple2)  # (1, 3, ['李信', '张飞'], '牛魔')
# 增加
tuple2[2].append("大乔")
print(tuple2)  # (1, 3, ['李信', '张飞', '大乔'], '牛魔')

# 8、定义只有一个元素的元组,需要带上逗号,否则会被识别为int、str等其它类型
tuple3 = (100)
tuple4 = (100,)
print(f"tuple3的类型是{type(tuple3)}")  # tuple3的类型是<class 'int'>
print(f"tuple4的类型是{type(tuple4)}")  # tuple4的类型是<class 'tuple'>


"""
9、列表操作起来更加方便,那么元组相较于列表的优势？
    1、在项目中，尤其是多线程环境中，有经验的程序员会考虑不变对象(一方面因为对象状态不能修改，所以可以
        避免由此引起的不必要的程序错误；另一方面一个不变对象自动就是线程安全的，这样就可以省掉处理
        同步化的开销。可以方便的被共享访问)。所以，如果不需要对元素进行增删改操作的话使用元组
    2、元组在创建时间和占用的空间上面都优于列表
    3、元组能够对不需要修改的数据保护
"""
