# 案例
# 定义变量
name = "jocker"
age = 18
score = 90.0
gender = "男"

# 1、%操作符
print("---" * 20)
print("1、%操作符使用方法")
print("个人信息：%s %d %s %.2f" % (name, age, gender, score))

# 2、format()函数
print("---" * 20)
print("2、format()函数使用方法")
print("个人信息：{} {} {} {}".format(name, age, score, gender))

# 3、f-strings
print("---" * 20)
print("3、f-strings使用方法")
print(f"个人信息：{name} {age} {score} {gender}")
