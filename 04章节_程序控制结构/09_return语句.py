"""
break语句、 continue语句和return语句的区别：
① 在循环体中，执行到break语句会终结离它最近的循环体，即：退出for循环或while循环
② 在循环体中，执行到continue语句会结束本次循环，即：进入下一轮循环，不会退出for循环或while循环
③ 在函数中，执行到return语句会跳出当前函数，即：函数中后面的代码不会再执行
"""

"""
- 说明
return作用在函数中，表示跳出所在的函数
"""


def f1():
    for i in range(1, 5):
        if i == 3:
            return
            # break
            # continue
        print("i =", i)
    print("结束循环")


f1()
"""
① return输出结果(跳出当前函数)
    i = 1
    i = 2
② break输出结果(终结当前循环体)
    i = 1
    i = 2
    结束循环
③ continue输出结果(结束本次循环)
    i = 1
    i = 2
    i = 4
    结束循环
"""
