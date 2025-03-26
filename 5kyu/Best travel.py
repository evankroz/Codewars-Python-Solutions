from itertools import combinations

def choose_best_sum(t, k, ls):
    sumarr = []
    #print(list(combinations(ls, k)))
    lst = list(combinations(ls, k))

    for comb in lst:
    #    print(comb)
        comb = list(comb)
        sumarr.append(sum(comb))
    
   # print(sumarr)

    if all(i>t for i in sumarr):
        return None
     
    new_arr = []
    for i in sumarr:
        if i<=t:
            new_arr.append(i)
        continue
    #print(new_arr)
    #print(max(new_arr))
    return max(new_arr)

#ts = [50, 55, 56, 57, 58]
#choose_best_sum(163, 3, ts)