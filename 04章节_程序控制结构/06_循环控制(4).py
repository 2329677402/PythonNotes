"""
多重循环练习题2
"""

print("---" * 20)
content1 = """
统计3个班成绩情况，每个班有5名同学，要求完成：
① 求出各个班的平均分和所有班级的平均分，学生的成绩从键盘输入
② 统计三个班及格人数
"""
print(f"demo1:{content1}")

"""
化繁为简
① 统计一个班成绩情况，求出一个班的平均分
② 统计三个班成绩情况，求出各个班平均分，所有班级平均分和及格人数
"""
print("---" * 20)
print("① 统计一个班成绩情况，求出一个班的平均分")
# 初始化班级总分
sum = 0.0
# 假设班级有5名学生
for i in range(5):
    score = float(input("请输入学生成绩："))
    sum += score
print(f"该班级平均分是：{sum / 5}")

print("---" * 20)
print("② 统计三个班成绩情况，求出各个班平均分，所有班级平均分和及格人数")
# 初始化所有班级总分
score_total = 0.0
# 初始化所有班级的及格人数
score_pass = 0
# 假设有三个班，使用for循环接收3个班的成绩
for j in range(3):
    # 初始化班级总分，注意：统计班级总分前，需要对成绩清零重置
    score_sum = 0.0
    # 假设班级有5名学生,使用for循环接收每个班的5名学生成绩
    for i in range(5):
        score = float(input(f"请输入第{j + 1}个班的第{i + 1}个学生的成绩："))
        # 获取及格人数
        if score >= 60.0:
            score_pass += 1
        # 获取班级总分
        score_sum += score
    print(f"第{j + 1}个班级平均分是：{score_sum / 5}")
    # 获取年级总分
    score_total += score_sum
# 输出年级平均分和及格人数
print(f"年级平均分是：{score_total / (5 * 3)},及格人数有{score_pass}个")

print("---" * 20)
print("③ 接收变量")
count_class = int(input("请输入需要统计的班级数量："))
count_student = int(input("请输入每个班需要统计的学生数量："))
# 初始化所有班级总分
score_total = 0.0
# 初始化所有班级的及格人数
score_pass = 0
for j in range(count_class):
    # 初始化班级总分，注意：统计班级总分前，需要对成绩清零重置
    score_sum = 0.0
    for i in range(count_student):
        score = float(input(f"请输入第{j + 1}个班的第{i + 1}个学生的成绩："))
        # 获取及格人数
        if score >= 60.0:
            score_pass += 1
        # 获取班级总分
        score_sum += score
    print(f"第{j + 1}个班级平均分是：{score_sum / count_student}")
    # 获取年级总分
    score_total += score_sum
# 输出年级平均分和及格人数
print(f"年级平均分是：{score_total / (count_student * count_class)},及格人数有{score_pass}个")

print("---" * 20)
content2 = "打印九九乘法表"
print(f"demo2:{content2}")
# i控制当前第几行
for i in range(1, 10):
    # j控制当前行等式的个数
    for j in range(1, 10):
        if j <= i:
            print(f"{i} * {j} = {i * j}", end="\t")
    print("")