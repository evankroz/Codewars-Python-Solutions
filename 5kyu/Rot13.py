def rot13(message) -> str:
    for abcd in ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]:
        message = ''.join([abcd[(abcd.index(char) + 13) % 26] if char in abcd
                           else char for char in message])
    print(message)
    return message

if __name__ == "__main__":
    message = 'test'
    rot13(message)

#resources used -> wikipedia :)
#https://en.wikipedia.org/wiki/ROT13