import re

def sum_of_integers_in_string(s):
    sum = 0
    y = re.findall("[0-9]+", s)

    for i in range(len(y)):
        sum += int(y[i])
    return sum