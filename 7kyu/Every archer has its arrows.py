def archers_ready(archers):
    count = 0
    if archers:
        for i in archers:
            if i >= 5:
                count += 1
    else:
        return False
    return count == len(archers)
