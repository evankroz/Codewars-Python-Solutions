def solve(a,b):
    res = ""
    for i in a:
        if i not in b:
            res += i
    for i in b:
        if i not in a:
            res += i
    return res
        
