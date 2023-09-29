def disarium_number(num):
    string = str(num)
    total = 0
    for i,j in enumerate(string):
        total += int(j) ** (i+1)
    if total == num:
        return "Disarium !!"
    return "Not !!"
