def consecutive(arr):
    if len(arr) == 1 or len(arr) == 0:
        return 0
    _max = max(arr)
    _min = min(arr)
    arr.remove(_max)
    arr.remove(_min)

    diff = _max-_min

    return (abs(len(arr)-diff+1))