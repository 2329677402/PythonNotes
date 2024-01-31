# +加, -减, *乘, /除, %取余, //取整除, **幂
# 对于 a/b ,返回结果是小数
print(10 / 3)  # 3.3333333333333335
# 对于 a//b ,返回商的整数部分(向下取整)
print(10 // 3)  # 3
print(-10 // 3)  # -4
# 对于 a%b ,对应公式：a % b = a - a // b * b
print(10 % 3)  # 1
print(-10 % 3)  # 2
print(10 % -3)  # -2
print(-10 % -3)  # -1
# 对于 a**b ,返回a的b次方
print(2 ** 5)  # 32

print("---" * 20)
# 算术运算符练习
print("作业一")
# 1、假如还有97天放假，问：合xx个星期零xx天
days = 97
week = days // 7
free_day = days % 7
print(f"假如还有{days}天放假,还有{week}个星期{free_day}天")

print("作业二")
# 2、定义一个变量保存华氏温度，华氏温度转换摄氏温度的公式为：5/9（华氏温-100），请求出华氏温度对应的摄氏温度。[234.5]
hua_shi = 234.5
she_shi = 5 / 9 * (hua_shi - 100)
print(f"华氏温度 {hua_shi} 对应的摄氏温度为 {she_shi} ")
print("华氏温度 %.2f 对应的摄氏温度为 %.2f" % (hua_shi, she_shi))
