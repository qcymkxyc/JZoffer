"""
    题目1
"""


def find_same1(nums = [1,2,3,2,1]):
    """
    查找相同的数
    :param nums:list
    :return:
    """
    same_list = list()
    for i,num in enumerate(nums):
        if num in nums[:i]:
            same_list.append(num)
    return same_list

def find_same2(nums):
    """
        冒泡排序解决
    :param nums:
    :return:
    """
    same_list = list()
    for i in range(len(nums)):
        for j in range(len(nums) - 1,i,-1):
            if nums[j] < nums[j - 1]:
                t = nums[j]
                nums[j] = nums[j - 1]
                nums[j - 1] = t
    for i,v in enumerate(nums):
        if i == len(nums) - 1:
            break
        if v == nums[i + 1]:
            same_list.append(v)
    return same_list