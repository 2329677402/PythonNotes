"""
集合生成式(用法参考列表生成式)
    1、集合生成式就是"生成集合的公式"
    2、基本语法
        {集合元素的表达式 for 自定义变量 in 可迭代对象}
        如:{i * 2 for i in range(1, 5)} -> 得到集合{2, 4, 6, 8}
"""
content = """
用三个集合表示三门学科的选课学生姓名(一个学生可以同时选多门课)
s_history = {'小明', '张三', '李四', '王五', 'Lily', 'Bob'}
s_politic = {'小明', '小花', '小红', '一狗'}
s_english = {'小明', 'Lily', 'Bob', 'Davil', '李四'}
- 求选课学生总共有多少人
- 求只选了第一个学科的学生数量和学生名字
- 求只选了一门学科的学生数量和学生名字
- 求选了三门学科的学生数量和学生名字
"""
print(f"demo:{content}")

s_history = {'小明', '张三', '李四', '王五', 'Lily', 'Bob'}
s_politic = {'小明', '小花', '小红', '一狗'}
s_english = {'小明', 'Lily', 'Bob', 'Davil', '李四'}

# T1
s_count = s_english | s_politic | s_history
print(len(s_count))  # 10

# T2
s_his = s_history - s_english - s_politic
print(len(s_his), s_his)  # 2 {'王五', '张三'}

# T3
# 分别求出只选择了各个学科的学生，然后求并集后自动去重
s_eng = s_english - s_politic - s_history
s_pol = s_politic - s_history - s_english
s_only = s_his | s_eng | s_pol
print(len(s_only), s_only)  # 6 {'小花', '小红', '张三', '一狗', 'Davil', '王五'}

# T4
s_all = s_history & s_english & s_politic
print(len(s_all), s_all)  # 1 {'小明'}
