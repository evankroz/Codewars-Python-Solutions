def reverse_number(n):
    n  = str(n) #converts number to string
    if int(n) < 0: #checks for negative values
        n = abs(int(n)) #if negative value, takes absolute value
        return int(str(n)[::-1]) * -1 #reverses string
    return int(n[::-1]) #reverses the string(integer) and then converts to int.
