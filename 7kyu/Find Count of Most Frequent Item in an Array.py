def most_frequent_item_count(array):
    if array == []:
        return 0
    max_res = []
    for i in array: 
        max_res.append(array.count(i))
    return max(max_res)





#input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
#ouptut: 5 