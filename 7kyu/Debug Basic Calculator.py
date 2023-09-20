def calculate (a, o, b):
        if o == "+":
            return a+b
        if o == "-":
            return a-b
        if o == "/":
            if b == 0:
                return None
            return a/b
        if o == "*":
            return a*b
        return None
