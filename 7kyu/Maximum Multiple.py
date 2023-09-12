def max_multiple(divisor, bound):
    #really slow code... ~2000ms
    res = []
    for i in range(0, bound+1):
        if i % divisor == 0:
            res.append(i)
    return max(res)

or

#faster, O(1)
def max_multiple(divisor, bound):
    return bound - (bound % divisor)

#https://www.codewars.com/kata/5aba780a6a176b029800041c/python
