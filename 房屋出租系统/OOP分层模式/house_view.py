"""
    说明:界面层：显示界面，接收用户输入，调用业务层方法
"""

from house_service import *
from utility import *


class HouseView:
    # 定义属性house_operation [业务层HouseService类]
    house_operation: HouseService = HouseService()

    def update_house(self):
        """
        功能:显示修改的页面，输入新的数据，修改对应的信息
        :return:
        """
        print("修改势力信息".center(32, "="))
        update_id = int(input("请输入待修改的势力排名(-1退出): "))
        if update_id == -1:
            print("放弃修改".center(32, "="))
            return

        # 根据输入的update_id返回对应的势力信息, 如果没有则返回None
        house: HouseData = self.house_operation.find_by_id(update_id)
        if house:
            # 如果直接回车，则保留原值;反之修改信息

            house.name = Utility.read_str(f"宗主({house.name}): ", house.name)
            house.phone = Utility.read_str(f"战力({house.phone}): ", house.phone)
            house.address = Utility.read_str(f"宗名({house.address}): ", house.address)
            house.rent = int(Utility.read_str(f"至尊位({house.rent}): ", house.rent))
            house.state = Utility.read_str(f"状态({house.state}): ", house.state)
            print("修改势力信息成功！".center(32, "="))
        else:
            print("未收录该势力，无法修改！".center(32, "="))

    def find_house(self):
        """
        功能:显示查找的界面，接收输入id，并显示对应的势力信息
        :return:
        """
        print("查找势力信息".center(32, "="))
        find_id = int(input("请输入要查找的势力排名: "))
        # 接收势力信息或返回None
        house = self.house_operation.find_by_id(find_id)
        if house:
            # 打印表头信息
            print("排名\t\t宗主\t\t战力\t\t\t\t宗名\t\t\t至尊位\t状态(未停战/已停战)")
            print(house)
        else:
            print(f"未收录排名为{find_id}的势力，查询失败！".center(32, "="))

    def del_house(self):
        """
        功能:删除势力信息，接收用户输入
        :return:
        """
        print("删除势力信息".center(32, "="))
        del_id = int(input("请输入待删除的编号(-1退出): "))
        if del_id == -1:
            print("放弃删除".center(32, "="))
            return

        # 接收删除信息y or n
        choice = Utility.read_confirm_select()

        # 确认是否删除
        if choice == 'y':
            # 调用service层的del_by_id方法
            if self.house_operation.del_by_id(del_id):
                # 执行删除
                print("删除成功".center(32, "="))
            else:
                print("未收录该势力，无法删除！".center(32, "="))
        else:
            print("放弃删除".center(32, "="))

    def add_house(self):
        """
        功能:显示添加的页面，接收用户输入，构建HouseData对象
        :return:
        """
        try:
            print("添加新晋势力".center(32, "="))
            name = input("宗主: ")
            phone = input("战力: ")
            address = input("宗名: ")
            rent = int(input("至尊位: "))
            state = input("状态(未停战/已停战): ")
            # 构建势力对象
            new_house = HouseData(0, name, phone, address, rent, state)
            # 调用Service方法，添加new_house
            self.house_operation.add(new_house)
            print("添加新晋势力成功！".center(32, "="))
        except ValueError:
            print("请正常添加势力信息！".center(32, "="))

    def list_houses(self):
        """
        功能:显示势力列表
        :return:
        """
        print("势力列表".center(32, "="))
        # 打印表头信息
        print("排名\t\t宗主\t\t战力\t\t\t宗名\t\t\t至尊位\t状态(未停战/已停战)")
        # 得到houses_list列表
        houses_list = self.house_operation.get_houses()
        # 遍历houses_list列表
        for i in houses_list:
            print(i)
        print("大千世界势力列表显示完毕!".center(32, "="))

    def exit_sys(self):
        """
        功能:完善退出系统
        :return: True or False
        """
        key = Utility.read_confirm_select()
        if key == 'y':
            return True
        else:
            return False

    def main_menu(self):
        """
        功能:显示主菜单
        :return:
        """
        while True:
            print()
            print("大千世界势力系统菜单".center(32, "="))
            print("\t\t1、新 增 势 力")
            print("\t\t2、查 找 势 力")
            print("\t\t3、删 除 势 力")
            print("\t\t4、修 改 势 力")
            print("\t\t5、势 力 列 表")
            print("\t\t6、退 出")
            key = input("道友请输入选择(1-6): ")
            if key in [str(i) for i in range(1, 7)]:
                if key == '1':
                    self.add_house()
                elif key == '2':
                    self.find_house()
                elif key == '3':
                    self.del_house()
                elif key == '4':
                    self.update_house()
                elif key == '5':
                    self.list_houses()
                elif key == '6':
                    if self.exit_sys():
                        break
            else:
                print("You can donate if you have bad eyes!")
