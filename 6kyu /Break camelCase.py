def solution(s):
    res = ""
    for i in s:
        if(i.isupper()):
            res += "-"+i
        else:
            res += i
    res = res.split("-")
    return " ".join(res)

#https://www.codewars.com/kata/5208f99aee097e6552000148
