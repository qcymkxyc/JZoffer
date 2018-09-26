"""
    题目一
"""
def find_same(nums):
    """

    :param nums:
    :return:
    """
    same_list = list()
    i = 0
    while i < len(nums):
        v = nums[i]
        if i == v:
            pass
        else:
            p = nums[v]
            if p == v:
                same_list.append(v)
            else:
                t = p
                nums[v] = v
                nums[i] = t
                i = 0
                continue
        i += 1
    return same_list


