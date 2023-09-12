def valid_braces(string):
    open = ["(", "{", "["]
    new = []
    for char in string:
        if char in open:
            new.append(char)
        else:
            if not new:
                return False
            current_char = new.pop()
            if current_char == "(":
                if char != ")":
                    return False
            if current_char == "{":
                if char != "}":
                    return False
            if current_char == "[":
                if char != "]":
                    return False
    if new:
        return False
    return True

#https://www.codewars.com/kata/5277c8a221e209d3f6000b56/python
