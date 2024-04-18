"""
    说明:数据层:HouseData类，一个HouseData对象对应一个房屋信息
"""


class HouseData:
    def __init__(self, id, name, phone, address, rent, state):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address
        self.rent = rent
        self.state = state

    # 重写__str__，按照指定格式输出对象
    def __str__(self):
        return f"{self.id}\t\t{self.name}\t\t{self.phone}\t\t{self.address}\t\t{self.rent}\t\t{self.state}"
