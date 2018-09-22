"""
    利用二分查找
"""

def f(n,num):
    row,col = len(n),len(n[0])
    low,high = 0,min(row,col) - 1

    while low <= high:
        mid = int((low + high) / 2)
        mid_num = n[mid][mid]
        if mid_num > num:
            high = mid - 1
            continue
        elif mid_num == num:
            return True
        else:
            #列查找
            sub_low,sub_high = mid,col - 1
            while sub_low <= sub_high:
                sub_mid = int((sub_low + sub_high) / 2)
                sub_mid_num = n[mid][sub_mid]
                if sub_mid_num > num:
                    sub_high = sub_mid - 1
                elif sub_mid_num == num:
                    return True
                else:
                    sub_low = sub_mid + 1

            #行查找
            sub_low,sub_high = mid,row - 1
            while sub_low <= sub_high:
                sub_mid = int((sub_low + sub_high) / 2)
                sub_mid_num = n[sub_mid][mid]
                if sub_mid_num > num:
                    sub_high = sub_mid - 1
                elif sub_mid_num == num:
                    return True
                else:
                    sub_low = sub_mid + 1

            low = mid + 1

    return False