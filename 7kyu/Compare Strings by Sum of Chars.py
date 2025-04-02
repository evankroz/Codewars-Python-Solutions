def compare(s1, s2):


    arr1 = []
    arr2 = []

    if s1 is not None:
        if all(c.isalpha() == True for c in s1):
            for i in s1:
                i = i.upper()
                arr1.append(ord(i))
        else:
            arr1 = [0]
    else:
        arr1 = [0]

    if s2 is not None:
        if all(c.isalpha() == True for c in s2):
            for j in s2:
                print(j)
                j = j.upper()
                arr2.append(ord(j))
                print(arr2)
        else:
            arr2 = [0]
    else:  
        arr2 = [0]
        
    print(arr1)
    print(arr2)
    print(sum(arr1) == sum(arr2))
    return sum(arr1) == sum(arr2)

compare("AD", "BC")
    