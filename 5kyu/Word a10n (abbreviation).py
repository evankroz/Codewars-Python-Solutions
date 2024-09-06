import re
def abbreviate(s):
    new_s = re.findall(r"[A-Za-z]+|\W+|[0-9]|[@#_]", s)
    a10n = []
    for i in new_s:
        if len(i) > 3 and i.isalpha():
            a10n.append(f"{i[0]}{len(i)-2}{i[-1]}")
        else:
            a10n.append(i)
    print("".join(a10n))
    return "".join(a10n)




'''
    abbreviate("elephant-rides are really fun!")
    // ^ ^ ^ ^ ^ ^ ^ ^ * ^ ^ ^ ^ ^ * ^ ^ ^ * ^ ^ ^ ^ ^ ^ * ^ ^ ^ *
    // words( ^):   "elephant" "rides" "are" "really" "fun"
    // 123456
    123
    1
    1234
    1
    // ignore
    short
    words: X
    X

    // abbreviate: "e6t"     "r3s"  "are"  "r4y"   "fun"
    // all
    non - word
    characters(*)
    remain in place
    // "-"      " "    " "     " "     "!"
    == = "e6t-r3s are r4y fun!"
'''
if __name__ == "__main__":
    s = "elephant-rides are really fun"
    abbreviate(s)