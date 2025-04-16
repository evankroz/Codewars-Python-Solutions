def meeting(s):
    pairs = [name.split(":")[::-1] for name in s.split(";")]
    pairs.sort(key=lambda x: (x[0].upper(), x[1].upper()))
    result = ''.join(f"({last.upper()}, {first.upper()})" for last, first in pairs)
    return result
            