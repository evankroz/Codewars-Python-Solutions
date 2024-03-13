def expanded_num(num):
    res = []

    for pos, int in enumerate(str(num)[::-1]):
        if int(int) != 0:
            res.append(int+"0"*pos)
        
    return " + ".join(res[::-1])