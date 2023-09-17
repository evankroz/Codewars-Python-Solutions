def reverse_alternate(s):
    return " ".join(i[::-1] if j%2 else i for j, i in enumerate(s.split()))
