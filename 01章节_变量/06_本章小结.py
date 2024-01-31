# 章节作业
print("---" * 20)
print("作业一")
# 1、程序阅读题，看看输出什么
n1 = 13
n2 = 17
n3 = n1 + n2
print("n3 =", n3)  # n3 = 30
n4 = 38
n5 = n4 - n3
print("n5 =", n5)  # n5 = 8

print("---" * 20)
print("作业二")
# 2、使用str类型，分别保存\n\t\r\\1 2 3等字符，并打印输出
str1 = '\n'
str2 = '\t'
str3 = '\r'
str4 = '\\'
str5 = '1'
print(r"\n的效果：", str1)
print(r"\t的效果：", str2)
print(r"\r的效果：", str3)
print(r"\\的效果：", str4)
print(r"1的效果：", str5)

print("---" * 20)
print("作业三")
# 3、保存两本书名，用+拼接;保存两本书价格，用加号拼接
book1_name = "西游记"
book1_price = 89.90
book2_name = "红楼梦"
book2_price = 139.70
print(book1_name + book2_name)
print(book1_price + book2_price)

print("---" * 20)
print("作业四")
# 4、编程实现如下效果
# 姓名  年龄  成绩  性别  爱好
# XX  XX  XX  XX  XX
# 要求：
# 1)用变量将姓名、年龄、成绩、性别、爱好存储
# 2)使用+
# 3)添加适当的注释
# 4)添加转义字符，使用一条语句输出

# 定义变量
name = "jocker"
age = 18
score = 90.0
gender = "男"
hobby = "打胶"

# 按需求输出信息
print("姓名\t\t年龄\t\t成绩\t\t性别\t\t爱好\n" + name
      + '\t' + str(age) + '\t\t' + str(score) + '\t'
      + gender + '\t\t' + hobby)
