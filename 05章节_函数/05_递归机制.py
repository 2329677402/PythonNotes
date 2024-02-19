"""
- 基本介绍
① 递归就是函数自己调用自己，每次调用时传入不同的值
② 递归有助于编程者解决复杂问题，同时可以让代码变得简洁

- 应用场景
① 各种数学问题如：八皇后问题，汉诺塔，阶乘问题，迷宫问题等等
    汉诺塔游戏规则:https://www.novelgames.com/zh/tower/
    八皇后游戏规则:https://www.novelgames.com/zh/queens/
    迷宫竞赛游戏规则:https://www.novelgames.com/zh/mazerace/

② 各种算法中也会使用到递归，比如快排，归并排序，二分查找，分治算法等
③ 将用栈解决的问题->递归代码比较简洁

- 重要规则
① 执行一个函数时，就创建一个新的空间(栈空间)
② 函数的变量是独立的，比如n变量
③ 递归必须向退出递归的条件逼近,否则就是无限递归,就会出现RecursionError:maximum recursion depth exceeded
④ 当一个函数执行完毕，或者遇到return，就会返回，遵守谁调用，就将结果返回给谁
"""


def dg(n):
    if n > 2:
        dg(n - 1)
    print("n =", n)


def dg2(n):
    if n > 2:
        dg2(n - 1)
    else:
        print("n =", n)


print("-----dg(4)-----")
dg(4)
# n = 2
# n = 3
# n = 4
print("-----dg2(4)-----")
dg2(4)


# n = 2

# 阶乘问题, n! = 1 * 2 * 3 * ... * (n - 1) * n
def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n


print("-----4的阶乘-----")
print(factorial(4))  # 24
