def capitalize(s):
    res1 = ""
    res2 = ""
    for i in range(len(s)):
        if i % 2 == 0:
            res1 += s[i].lower()
        else:
            res1 += s[i].upper()
    for l in range(len(s)):
        if l % 2 ==0:
            res2 += s[l].upper()
        else:
            res2 += s[l].lower()
    return [res2, res1]

#https://www.codewars.com/kata/59cfc000aeb2844d16000075/python
