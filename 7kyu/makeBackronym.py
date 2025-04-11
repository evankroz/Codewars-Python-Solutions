#preloaded variable: "dictionary"

def make_backronym(acronym):
    #dictionary = 0
    wrd_lst = []
    for i in acronym:
        wrd_lst.append(dictionary[i.upper()])
    return " ".join(wrd_lst)