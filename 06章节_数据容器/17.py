# 1、随机生成10个整数(1-100)保存到列表中，使用冒泡排序，对其从大到小排序.
import random

num_list = []
# 生成随机列表
for i in range(10):
    num_list.append(random.randint(1, 100))
print("随机生成的列表为:", num_list)


# 冒泡排序函数
def bubble_sort(my_list):
    """
    :param my_list: 要排序的列表(从大到小).
    :return: 无
    """
    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - 1 - i):
            if my_list[j] < my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
        print(f"第{i + 1}轮排序结果:", my_list)


bubble_sort(num_list)


# 2、使用二分查找，查找是否有8这个数，如果有，返回对应的下标，否则返回-1.
# 二分查找函数
def binary_search(my_list, find_val):
    """
    :param my_list: 要查找的列表(从大到小).
    :param find_val: 要查找的元素.
    :return: 如果找到返回对应的下标,如果没找到,返回-1.
    """
    # 初始化最左/右边的索引下标
    left_index, right_index = 0, len(my_list) - 1
    # 定义需要查找元素的下标
    find_index = -1
    # 使用while循环,不断折半比较中间值,比较的前提是满足:left_index <= right_index.
    while left_index <= right_index:
        # 定义中间数的索引
        mid_index = (left_index + right_index) // 2

        if my_list[mid_index] < find_val:
            right_index = mid_index - 1

        elif my_list[mid_index] > find_val:
            left_index = mid_index + 1

        else:
            find_index = mid_index
            break
    else:
        print(f"未在列表中找到{find_val}！")
    return find_index


res_index = binary_search(num_list, 8)
print("res_index:", res_index)
