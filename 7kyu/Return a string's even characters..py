def even_chars(st): 
    if len(st) < 2 or len(st) > 100:
        return "invalid string"
    return list(st[1::2])
