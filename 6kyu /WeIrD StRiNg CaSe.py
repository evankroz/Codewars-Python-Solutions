def to_weird_case(words):
    words = words.split(' ')
    new_words = []
    for word in words:
        new_word = ''
        for i, char in enumerate(word):
            if i % 2 == 0:
                new_word += char.upper()
            else:
                new_word += char.lower()
        new_words.append(new_word)
    return ' '.join(new_words)
