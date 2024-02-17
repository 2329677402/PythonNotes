# 章节作业
print("---" * 20)
content = """
某人有100,000元，每经过一次路口，需要缴费，规则如下：
当现金>50000时，每次交5%
当现金<=50000时，每次交1000
计算此人可以经过多少次路口，使用while + break方式完成
"""
print(f"demo:{content}")
# 初始化路口次数
count = 0
# 初始化余额
money = 100000
while True:
    if money > 50000:
        money -= money * 0.05
        count += 1
        print(f"第{count}次经过路口,还剩余额{money}")
    elif 1000 <= money <= 50000:
        money -= 1000
        count += 1
        print(f"第{count}次经过路口,还剩余额{money}")
    else:
        break
print(f"此人可以经过{count}次路口，剩余的钱为{money}，不足1000")
