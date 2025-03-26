def next_happy_year(year):
    year += 1
    while not len(set(str(year))) == len(str(year)):
        year += 1

    print(year)
    return year

next_happy_year(1001)
