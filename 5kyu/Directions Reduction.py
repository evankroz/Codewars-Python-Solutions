def dir_reduc(arr):
    opp = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST"
    }
    stack = []
    for direction in arr:
        if stack and opp[direction] == stack[-1]:
            stack.pop()
        else:
            stack.append(direction)
    print(stack)
    return stack


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
dir_reduc(a)