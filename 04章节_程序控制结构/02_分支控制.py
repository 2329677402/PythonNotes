"""
分支结构有：单分支、 双分支、 多分支、 嵌套分支
"""

"""
① 单分支基本语法
单分支是通过if语句来实现的, if语句的基本语法如下:
if 条件表达式:
    代码块 (可以有多条语句)

- 说明
1、当条件表达式为True时，就会执行代码块；如果为False，就不执行
2、Python缩进非常重要，是用于界定代码块的，相当于其他编程语言里的大括号{}
3、最短的缩进对较长的有包含关系，缩进前后没有要求，但是每个代码块应具有相同的缩进长度(TAB或者相同个数的空格）
4、小结：可以看出，和其它语言对比：其它语言的代码块是用{}表示的，python则是缩进代替了{}
"""
print("---" * 20)
content1 = "请编写一个程序，可以输入人的年龄，如果该小伙伴的年龄大于18岁,则输出“你年龄大于18,要对自己的行为负责！”"
print(f"demo1：{content1}")
age = int(input("请输入你的年龄："))
if age > 18:
    print("你年龄大于18,要对自己的行为负责！")

"""
② 双分支基本语法
if 条件表达式:
    代码块1
else:
    代码块2
    
- 说明
1、if、else是关键字，是规定好的
2、当条件表达式成立，即执行代码块1，否则执行代码块2，注意，不要少写了冒号：
"""
print("---" * 20)
content2 = "编写一个程序，可以输入人的年龄，如果该小伙伴的年龄大于18岁，则输出“你年龄大于18，要对自己的行为负责！”。否则，输出“你的年龄不大，这次放过你了”"
print(f"demo2:{content2}")
age = int(input("请输入你的年龄："))
if age > 18:
    print("你年龄大于18,要对自己的行为负责！")
else:
    print("你的年龄不大，这次放过你了")

"""
③ 多分支基本语法
if 条件表达式1:
    代码块1
elif 条件表达式2:
    代码块2
......
else:
    代码块n
"""
print("---" * 20)
content3 = """
小头儿子参加python考试，他和大头爸爸达成承诺：
如果：
成绩为100分时，奖励一辆BMW；
成绩为(80,99]时，奖励一台iphone13；
当成绩为[60,80]时，奖励一个iPad；
其它时，什么奖励也没有。
请从键盘输入小头儿子的期末成绩，并加以判断
"""
print(f"demo3:{content3}")
score = int(input("请输入你的分数："))
# 注意：Python支持将score >=0 and score <= 100的语句简化为0 <= score <= 100的语句格式
if 0 <= score <= 100:
    if score == 100:
        print("奖励一台BMW")
    elif 80 < score <= 99:
        print("奖励一台iPhone")
    elif 60 <= score <= 80:
        print("奖励一台iPad")
    else:
        print("没有奖励")
else:
    print("你输入的分数不合法")

"""
④ 嵌套分支基本语法
if 条件表达式1:
    if 条件表达式2:
    #if-else...
    else:
    #if-else...
else:
    代码块
- 说明
1、嵌套分支：在一个分支结构中又嵌套了另一个分支结构
2、里面的分支的结构称为内层分支，外面的分支结构称为外层分支
3、规范：不要超过3层（可读性不好）
"""
print("---" * 20)
content4 = """
1、参加歌手比赛，如果初赛成绩大于8.0进入决赛，否则提示淘汰。并且根据性别提示进入男子组或女子组,输入成绩和性别，进行判断和输出信息。
"""
print(f"demo4:{content4}")
score = float(input("请输入你的初赛分数："))
if 0 <= score <= 10.0:
    if score > 8.0:
        print("恭喜，你已进入决赛")
        gender = input("请输入你的性别：")
        if gender == "男" or "boy":
            print("你已被分配到男子组")
            print(f"你的成绩是：{score}, 你的性别是：{gender}")
        elif gender == "女" or "girl":
            print("你已被分配到女子组")
            print(f"你的成绩是：{score}, 你的性别是：{gender}")
        else:
            print("你的性别不符合当前比赛的报名机制，请回炉重造！！！")
    else:
        print("抱歉，你已被淘汰")
else:
    print("你输入的分数不合法")

print("---" * 20)
content5 = """
2、出票系统：根据淡旺季的月份和年龄，打印票价
4-10旺季：
成人（18-60）：60
儿童（<18）：半价
老人（>60）：1/3
淡季：
成人：40
其他：20
"""
print(f"demo5:{content5}")
year = int(input("请输入你的年龄："))
if year >= 0:
    month = int(input("请输入当前月份："))
    if 4 <= month <= 10:
        if 0 <= year < 18:
            print("当前你的票价是：30")
        elif 18 <= year <= 60:
            print("当前你的票价是：60")
        else:
            print("当前你的票价是：20")
    elif 1 <= month < 4 or 10 < month <= 12:
        if 18 <= year <= 60:
            print("当前你的票价是：40")
        else:
            print("当前你的票价是：20")
    else:
        print("你输入的月份不合法！")
else:
    print("你输入的年龄不合法！")
