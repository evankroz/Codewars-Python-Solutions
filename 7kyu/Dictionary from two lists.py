def create_dict(keys, values):
    result = {}
    len_keys = len(keys)
    len_vals = len(values)
    for i in range(len_keys):
        if i < len_vals:
            key = keys[i]
            value = values[i]
        else:
            key = keys[i]
            value = None
        result[key] = value
    return result
    
create_dict([1,2,3], ["1", "2", "3"])