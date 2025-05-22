def is_divisible(*args):
    l = []
    for i in range(1, len(args)):
        l.append(args[0]%args[i])
        print(l)
    
    return l == [0]*len(l)

print(is_divisible(12,3,4))
    