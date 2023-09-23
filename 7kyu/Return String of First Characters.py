def make_string(s):
    new = []
    s = s.split(" ")
    for i in s:
        new.append(i[0])
    return "".join(new)
