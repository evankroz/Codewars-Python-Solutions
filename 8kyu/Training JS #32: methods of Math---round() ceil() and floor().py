import math

def round_it(n):
    i = str(n)
    res = i.split(".")
    #print(res)
    if len(res[0])>len(res[1]):
        return math.floor(n)
    if len(res[0])<len(res[1]):
        return math.ceil(n)
    return round(n)