"""
字符串比较
    1、运算符: >, >=, <, <=, ==, !=
    2、比较规则:首先比较两个字符串中的第一个字符,如果相等则继续比较下一个字符,依次比较下去,直到不等时,就是比较结果
    3、比较原理:依据字符对应的ordinal value,也就是码值大小来判定 (Unicode码值上限65536)
        ord()函数用于将字符转换为码值
        chr()函数用于将码值转换为字符
"""
print(ord('9'))  # 57
print(ord('瑶'))  # 29814

print(chr(57))  # 9
print(chr(29814))  # 瑶

print('tom' > 'jack')  # True

print("---" * 20)
content = """
定义一个字符串,str_names = "tom jack mary nono smith hsp",
- 统计一共有多少人名
- 如果有'hsp',替换为'老韩'
- 如果人名是英文,把首字母改为大写
"""
print(f"demo:{content}")

str_names = "tom jack mary nono smith hsp"
list1 = str_names.split(" ")
print(list1)
print(len(list1))  # 6

str1 = str_names.replace('hsp', '老韩')
print(str1)  # tom jack mary nono smith 老韩

str2 = ""
print(id(str2))  # 1673854943280
for i in list1:
    # isalpha方法:如果字符串中的所有字符都为字符并且至少有一个字符则返回True,否则返回False.
    if i.isalpha():
        # capitalize方法:返回原字符串的副本,首字符大写,其余小写.
        # 将list1中遍历的元素追加到空字符串str2中,并以" "符号间隔
        str2 += i.capitalize() + " "
        print(id(str2))
# 注意:字符串虽然是不可变序列,但通过id()函数可观察到str2每次加入元素内存地址都会变化;
# 说明str2字符串名虽然未变,但每次遍历之后都是新的对象.
print(str2.strip())  # Tom Jack Mary Nono Smith Hsp
print(id(str2.strip()))  # 2848325705504
