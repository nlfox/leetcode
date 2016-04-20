def delDupList(ls):
    retList = []
    ret = []
    for l in ls:
        l.sort()
        sL = ','.join([str(i) for i in l])
        if sL not in retList:
            retList.append(sL)

    for i in retList:
        ret.append([int(j) for j in i.split(",")])
    return ret

lists = [[7], [10, 6], [1, 1, 5], [1, 5, 1], [2, 5], [1, 1, 5], [5, 2], [5, 1, 1], [6, 1], [1, 5, 1], [5, 1, 1]]
print delDupList(lists)
