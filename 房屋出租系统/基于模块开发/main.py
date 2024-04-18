"""
    说明:大千世界势力系统的主程序
"""

# 导入模块
from house_operation import *


def main():
    """
    主函数，程序的执行入口
    :return:
    """
    # 调用main_menu函数显示主菜单
    # 循环显示菜单
    while True:
        main_menu()
        key = input("道友请输入选择(1-6): ")
        if key in [str(i) for i in range(1, 7)]:
            if key == '1':
                add_houses()
            elif key == '2':
                find_houses()
            elif key == '3':
                del_houses()
            elif key == '4':
                update_houses()
            elif key == '5':
                list_houses()
            elif key == '6':
                if exit_sys():
                    break
        else:
            print("You can donate if you have bad eyes!")


# 测试
if __name__ == "__main__":
    main()
    print("See you again!")
