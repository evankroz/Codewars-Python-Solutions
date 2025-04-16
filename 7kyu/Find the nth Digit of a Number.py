def find_digit(num, nth):
    num = abs(num)
    if nth <=  0:
        return -1
    num = list(str(num))
    arr = [int(i) for i in num]
    
    try:
        print(arr[-1*nth])
        return arr[-1*nth]
    except:
        print(0)
        return 0



find_digit(5673, 4)