def generate_hashtag(s):
    if s == "":
        return False
    final = "#" + s.title().replace(" ", "")
    if len(final) > 140:
        return False
    return final
