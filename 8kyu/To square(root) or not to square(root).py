def square_or_square_root(arr):
    res = []
    for i in arr:
        if i ** 0.5 == int(i ** 0.5):
            res.append(i ** 0.5)
        else:
            res.append(i ** 2)
    return res
