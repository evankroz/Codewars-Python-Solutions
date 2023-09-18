def factors(x):
    if type(x) != int:
        return -1
    if x <= 0:
        return -1
    res = []
    for i in range(1,x+1):
        if x % i == 0:
            res.append(i)
    return sorted(res, reverse = True)
