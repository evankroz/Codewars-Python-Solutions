def find_smallest(numbers,to_return):
    return numbers.index(min(numbers)) if to_return == "index" else min(numbers)
