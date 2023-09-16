def data_reverse(data):
    n=[]
    res=[]
    for i in range(0,len(data),8):
	    n.append(data[i:i + 8])
    for i in reversed(n):
	    res.extend(i)
    return res
