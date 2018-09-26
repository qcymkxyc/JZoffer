"""
    题目2
"""
def find_same1(nums):
    """

    :param nums:
    :return:
    """
    nums_set = set()
    same_list = list()
    for num in nums:
        if num in nums_set:
            same_list.append(num)
        else:
            nums_set.add(num)
    return same_list

def find_same2(nums):
    """
    利用直接插入排序
    :param nums:
    :return:
    """
    same_list = list()
    temp = list()
    for num in nums:
        flag = True
        for i,temp_num in enumerate(temp):
            if temp_num > num:
                temp.insert(i,num)
                flag = False
                break
            elif temp_num == num:
                same_list.append(num)
                flag = False

        if flag:
            temp.append(num)

    return same_list



