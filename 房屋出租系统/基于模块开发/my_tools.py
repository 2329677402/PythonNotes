"""
    说明:编写工具函数
"""


def read_confirm_select():
    """
    功能:接收确认信息(Y/N)，不区分大小写，如果不是Y/N,则再次输入直到符合接收条件
    :return: y or n
    """
    print("请确认输入选择(Y/N): ", end="")
    while True:
        key = input()
        if key.lower() == 'y' or key.lower() == 'n':
            break
        else:
            print("选择无效,请重新输入(Y/N): ", end="")
    return key.lower()


def read_str(tip, default_val):
    """
    功能:读取用户输入信息，如果用户未输入，则返回默认信息default_val
    :param tip: 输入提示信息
    :param default_val: 默认值
    :return:
    """
    str = input(tip)
    if len(str) > 0:
        return str
    else:
        return default_val
