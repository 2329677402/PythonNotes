# and与, or或, not非
# 定义变量
a = 10
b = 20
c = 0
# 对于x and y,如果x为False,x and y返回x的值，否则返回y的计算值
print(a and b)  # 20
print(c and b)  # 0
# 对于x or y,如果x是True,它返回x的值，否则它返回 y的计算值
print(a or b)  # 10
print(c or b)  # 20
# 对于not x,如果x为True,返回 False，如果x为False，则返回 True
print(not (a and b))  # False
