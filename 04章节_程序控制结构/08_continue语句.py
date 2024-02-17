"""
- 说明
1、continue语句是用在for或while循环所嵌套的代码
2、continue语句用于结束本次循环，继续执行循环的下一个轮次
    注意：继续执行的是该continue最近的外层循环的下一个轮次
"""
i = 1
while i <= 4:
    i += 1
    if i == 3:
        continue
    print("i =", i)
# i = 2
# i = 4
# i = 5

for i in range(0, 2):
    for j in range(1, 4):
        if j == 2:
            continue
        print("i =", i, "j =", j)
# i = 0 j = 1
# i = 0 j = 3
# i = 1 j = 1
# i = 1 j = 3
