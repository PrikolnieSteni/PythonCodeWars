
def zero(item = None): return 0 if not item else item(0)
def one(item = None): return 1 if not item else item(1)
def two(item = None): return 2 if not item else item(2)
def three(item = None): return 3 if not item else item(3)
def four(item=None): return 4 if not item else item(4)
def five(item = None): return 5 if not item else item(5)
def six(item = None): return 6 if not item else item(6)
def seven(item = None): return 7 if not item else item(7)
def eight(item = None): return 8 if not item else item(8)
def nine(item = None): return 9 if not item else item(9)

def plus(item):
    return lambda x: x+item
def minus(item):
    return lambda x: x - item
def times(item):
    return lambda x: x * item
def divided_by(item):
    return lambda x: int(x / item)

print(seven(times(five())))