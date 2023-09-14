def in_array(array1, array2):
    res = []
    for i in array2:
        for j in array1:
            if j in i:
                res.append(j)
    for i in sorted(res):
        while res.count(i) > 1:
            res.remove(i)
    return sorted(res)

#https://www.codewars.com/kata/550554fd08b86f84fe000a58/python
