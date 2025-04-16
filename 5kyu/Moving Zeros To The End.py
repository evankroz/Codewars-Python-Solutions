def move_zeros(lst):
    res = lst.copy()
    count = 0
    for i in lst:
        if i == 0:
            res.remove(i)
            count += 1

    for _ in range(count):
        res.append(0)

    print(res)
    return res

move_zeros([0,2,1,0])