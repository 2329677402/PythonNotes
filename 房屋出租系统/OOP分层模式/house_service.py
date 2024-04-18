"""
    说明:业务层:提供对势力操作的方法
"""

from house_data import *


class HouseService:
    # 定义属性houses_list列表，存放势力信息
    houses_list = []
    # 定义属性id_counter：记录当前势力排名
    id_counter = 1

    def __init__(self):
        # 加入测试数据
        house = HouseData(1, "萧炎", "202404", "无尽火域", 80, "已停战")
        self.houses_list.append(house)

    def get_houses(self):
        """
        功能:返回势力列表
        :return:
        """
        return self.houses_list

    def add(self, new_house: HouseData):
        """
        功能:将接收到的new_house添加到houses_list中
        :param new_house: 新增对象
        :return:
        """
        # 分配id给new_house
        self.id_counter += 1
        new_house.id = self.id_counter
        return self.houses_list.append(new_house)

    def find_by_id(self, find_id):
        """
        功能:根据find_id返回对应的HouseData对象，不存在返回None
        :param find_id: 势力排名
        :return: HouseData对象或None
        """
        # 遍历houses_list
        for house in self.houses_list:
            if find_id == house.id:
                return house
        # 如果houses_list中没有找到find_id，默认返回None

    def del_by_id(self, del_id):
        """
        功能:根据接收到的del_id删除对应势力
        :param del_id: 势力排名
        :return: True删除成功 or False删除失败(未找到del_id)
        """
        # 判断del_id是否存在
        house = self.find_by_id(del_id)
        if house is None:
            return False
        else:
            # 找到del_id执行删除操作
            self.houses_list.remove(house)
            return True
