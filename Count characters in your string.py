def count(string):
    result = {char: string.count(char) for char in list(string)}
    return result