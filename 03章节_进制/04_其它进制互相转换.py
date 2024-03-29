"""
① 二进制转八进制
规则：从低位开始，将二进制数每三位一组，转成对应的八进制数即可
demo1：将0b11010101转成八进制
0b11010101 = 0o(0b011 0b010 0b101) = 0o325

② 二进制转十六进制
规则：从低位开始，将二进制数每四位一组，转成对应的十六进制数即可
demo2：将0b11010101转成十六进制
0b11010101 = 0x(0b1101 0b0101) = 0xD5

③ 八进制转二进制
规则：将八进制数每1位，转成对应的一个3位的二进制数即可
demo3：将0o237转成二进制
0o237 = 0b(0o2 0o3 0o7) = 0b(010 011 111) = 0b10011111

④ 十六进制转二进制
规则：将十六进制数每1位，转成对应的一个4位的二进制数即可
demo4：将0x23B转成二进制
0x23B = 0b(0o2 0o3 0oB) = 0b(0010 0011 1011) = 0b1000111011
"""

# 验证
print(oct(0b11010101))  # 0o325
print(hex(0b11010101))  # 0xd5
print(bin(0o237))  # 0b10011111
print(bin(0x23B))  # 0b1000111011
