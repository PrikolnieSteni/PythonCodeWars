def duplicate_count(text):
    rez = len({char: text.lower().count(char) for char in text if text.lower().count(char)>1}.values())
    return  rez

print(duplicate_count('asafffd'))