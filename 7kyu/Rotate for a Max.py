def max_rot(n):
    s =str(n)
    max_num = n
    current = s
    for k in range(len(s)-1):
        rotated_part = current[k+1:] + current[k]
        current = current[:k] + rotated_part
        current_num = int(current)
        if current_num>max_num:
            max_num = current_num
    return max_num