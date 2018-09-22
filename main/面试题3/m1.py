def f(n,num):
    row,col = len(n),len(n[0])
    m = min(len(n),len(n[0]))

    flag = False
    for i in range(m):
        #行
        for j in range(i,row):
            if n[j][i] == num:
                flag = True
                break;
            if n[j][i] > num:
               break
        for j in range(i,col):
            if n[i][j] == num:
                flag = True
                break
            if n[i][j] > num:
                break

        if flag:
            break
    return flag
