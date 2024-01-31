# ==等于, !=不等于, <小于, >大于, <=小于等于, >=大于等于, is判断两个变量引用对象是否相同, is not判断两个变量引用对象是否不同
a = 10
b = 1
print(a > b)  # True
print(a >= b)  # True
print(a < b)  # False
print(a <= b)  # False
print(a == b)  # False
print(a != b)  # True
flag = a > b
print("flag =", flag)  # flag = True
print(a is b)  # False
print(a is not b)  # True

print("---" * 20)
# 扩展：== 与 is 的区别
# 在检查 a is b 的时候，其实相当于检查 id(a) == id(b)。而检查 a == b 的时候，实际是调用了对象 a 的 __eq()__ 方法，a == b 相当于 a.__eq__(b)
# is 是比 == 更严格的检查，只要 a 和 b 的值相等，a == b 就会返回True，而只有 id(a) 和 id(b) 相等时，a is b 才返回 True
a = "hello"
b = "hello"
print(id(a))
print(id(b))
print(a is b)  # 输出 True
print(a == b)  # 输出 True

a = "hello world"
b = "hello world"
print(id(a))
print(id(b))
# Python中当字符串中出现了非标识符允许的字符的时候不采取驻留，即空格，如果把"hello world"改成"hello_world"， 在cmd命令下a is b还是返回 true，只是因为字符中存在一个空格所以才不采用驻留机制
print(a is b)  # 输出 True,注意：在cmd命令行下会返回False,其指向的内存地址也会不同,这是因为Pycharm对Python的字符串驻留机制进行了优化
print(a == b)  # 输出 True

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a is b)  # 输出 False
print(a == b)  # 输出 True

a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(a is b)  # 输出 True
print(a == b)  # 输出 True
