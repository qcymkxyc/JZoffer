def find_same(nums):
    """
    采用二分查找的方式
    :param nums:
    """
    size = len(nums)
    high = size
    low = 1

    while low < high:
        mid = (low + high) // 2

        count = 0
        for num in nums:
            if num < mid:
                count += 1

        if count > mid:
            high = mid
        else:
            low = mid + 1

    return low
