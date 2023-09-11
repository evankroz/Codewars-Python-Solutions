def duplicate_encode(word):
    word = word.lower()
    res = ""
    for l in word:
        if word.count(l) > 1:
            res += ")"
        if word.count(l) == 1:
            res += "("
    return res
