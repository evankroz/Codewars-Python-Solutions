def longest_consec(strarr, k):
    n = len(strarr)
    if strarr == [] or k <= 0 or k > n:
        return ""
    if k == 1:
        return sorted(strarr, key=len)[::-1][0]
    
    longest = index = 0


    for i in range(n-k+1):
        length = sum([len(s) for s in strarr[i:i+k]])
        if length > longest:
            longest = length
            index = i
        
    return ''.join(strarr[index:index+k])
