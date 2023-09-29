def last_survivor(letters, coords): 
    res = list(letters)
    for i in coords:
        res.pop(i)
    return "".join(res)
