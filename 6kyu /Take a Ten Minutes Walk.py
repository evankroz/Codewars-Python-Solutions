def is_valid_walk(walk):
    if len(walk) > 10:
        return False
    x_cord = 0
    y_cord = 0
    for i in walk:
        if i == "n":
            x_cord += 0
            y_cord += 1
        if i == "s":
            x_cord += 0
            y_cord -= 1
        if i == "e":
            x_cord += 1
            y_cord += 0
        if i == "w":
            x_cord -= 1
            y_cord += 0
    return x_cord == 0 and y_cord == 0 and len(walk) == 10

#https://www.codewars.com/kata/54da539698b8a2ad76000228/python
