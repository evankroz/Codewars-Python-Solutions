def reverse_letter(string):
    res = []
    for i in string:
        if i.isalpha():
            res.append(i)
    return "".join(res[::-1])
#https://www.codewars.com/kata/58b8c94b7df3f116eb00005b/python
