def zipvalidate(postcode):
    if len(postcode) != 6:
        return False
    num = ["0","5","7","8","9"]
    if postcode[0] in num:
        return False
    for i in postcode:
        if i.isdigit() == False:
            return False
    return True
