def f(n,num):
    row,col = len(n),len(n[0])
    z = n[0][col - 1]
    if z > num:
        sub_n = [s[:-1] for s in n]
        return f(sub_n,num)
    elif z == num:
        return True
    else:
        sub_n = n[1:]
        return f(sub_n,num)


