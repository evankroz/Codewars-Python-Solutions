def count_change(m, c):
    if m == 0:
        return 1
    if len(c) <= 0 or m < 0:
        return 0
    else:
        return count_change(m-c[0], c) + count_change(m, c[1:])

 # https://www.codewars.com/kata/541af676b589989aed0009e7/python
