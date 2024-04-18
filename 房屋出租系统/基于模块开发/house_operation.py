"""
    说明:提供对大千世界势力的各种操作
"""
from my_tools import *


def main_menu():
    """
    功能:显示主菜单页面
    :return:
    """
    print()
    print("大千世界势力系统菜单".center(32, "="))
    print("\t\t1、新 增 势 力")
    print("\t\t2、查 找 势 力")
    print("\t\t3、删 除 势 力")
    print("\t\t4、修 改 势 力")
    print("\t\t5、势 力 列 表")
    print("\t\t6、退 出")


# 定义全局变量houses_list，并加入两条初始的测试数据
houses_list = [{"id": 1, "name": "萧炎", "phone": "176********",
                "address": "无尽火域", "rent": 80, "state": "已停战"},
               {"id": 2, "name": "林动", "phone": "138********",
                "address": "武   境", "rent": 60, "state": "未停战"}]


def list_houses():
    """
    功能:显示势力列表
    :return:
    """
    print("势力列表".center(32, "="))
    # 打印表头信息
    print("排名\t\t宗主\t\t战力\t\t\t\t宗名\t\t\t至尊位\t状态(未停战/已停战)")

    # 遍历houses_list列表
    for house_msg in houses_list:
        # 遍历取出的字典对象的value值
        for value in house_msg.values():
            print(value, end="\t\t")
        # 输出一个完整的house信息后换行
        print()
    print("大千世界势力列表显示完毕!".center(32, "="))


# 定义全局变量id_counter,记录当前势力的id
id_counter = 2


def add_houses():
    """
    功能:添加势力信息
    :return:
    """
    try:
        print("添加新晋势力".center(32, "="))
        name = input("宗主: ")
        phone = input("战力: ")
        address = input("宗名: ")
        rent = int(input("至尊位: "))
        state = input("状态(未停战/已停战): ")

        # 声明全局变量
        global id_counter
        # 由系统分配每次添加新晋势力后的id_counter，即:每新增一次id，自增1
        id_counter += 1
        # 构建势力信息对应的字典对象，并加入到全局变量houses_list中
        house = {"id": id_counter, "name": name, "phone": phone,
                 "address": address, "rent": rent, "state": state}
        houses_list.append(house)
        print("添加新晋势力成功！".center(32, "="))
    except ValueError:
        print("请正常添加势力信息！".center(32, "="))


def find_by_id(find_id):
    """
    功能:根据输入的find_id返回对应的势力信息(字典),如果没有则返回None
    :param find_id: 势力列表houses_list中字典对象house的id值
    :return: 字典对象house or None
    """
    # 遍历houses_list列表
    for house in houses_list:
        if house["id"] == find_id:
            return house
    # 如果没有return，默认返回None
    # return None


def del_houses():
    """
    功能:删除势力信息
    :return:
    """
    print("删除势力信息".center(32, "="))
    del_id = int(input("请输入待删除的编号(-1退出): "))
    if del_id == -1:
        print("放弃删除".center(32, "="))
        return

    # 接收删除信息y or n
    choice = read_confirm_select()

    # 确认是否删除
    if choice == 'y':
        # 根据del_id去houses_list列表中查找是否存在该势力
        house = find_by_id(del_id)
        # house为None时，对应的布尔值为False，if语句不执行；反之正常执行
        if house:
            # 执行删除
            houses_list.remove(house)
            print("删除成功".center(32, "="))
        else:
            print("未收录该势力，无法删除！".center(32, "="))
    else:
        print("放弃删除".center(32, "="))


def update_houses():
    """
    功能:修改势力信息
    :return:
    """
    print("修改势力信息".center(32, "="))
    update_id = int(input("请输入待修改的势力排名(-1退出): "))
    if update_id == -1:
        print("放弃修改".center(32, "="))
        return

    # 根据输入的update_id返回对应的势力信息(字典), 如果没有则返回None
    house = find_by_id(update_id)
    if house:
        # 如果直接回车，则保留原值;反之修改信息

        # name = input(f"宗主({house['name']}): ")
        # if len(name) > 0:
        #     house['name'] = name

        # 使用read_str方法将以上重复代码封装起来简化步骤
        house['name'] = read_str(f"宗主({house['name']}): ", house['name'])
        house['phone'] = read_str(f"战力({house['phone']}): ", house['phone'])
        house['address'] = read_str(f"宗名({house['address']}): ", house['address'])
        house['rent'] = int(read_str(f"至尊位({house['rent']}): ", house['rent']))
        house['state'] = read_str(f"状态({house['state']}): ", house['state'])
        print("修改势力信息成功！".center(32, "="))
    else:
        print("未收录该势力，无法修改！".center(32, "="))


def find_houses():
    """
    功能:根据id查找势力信息
    :return:
    """
    print("查找势力信息".center(32, "="))
    find_id = int(input("请输入要查找的势力排名: "))
    # 接收势力信息或返回None
    house = find_by_id(find_id)
    if house:
        # 打印表头信息
        print("排名\t\t宗主\t\t战力\t\t\t\t宗名\t\t\t至尊位\t状态(未停战/已停战)")
        for i in house.values():
            print(i, end="\t\t")
        print()
    else:
        print(f"未收录排名为{find_id}的势力，查询失败！".center(32, "="))


def exit_sys():
    """
    功能:完善退出确认功能
    :return: True or False
    """
    # 接收退出信息y or n
    choice = read_confirm_select()
    if choice == 'y':
        return True
    else:
        return False
