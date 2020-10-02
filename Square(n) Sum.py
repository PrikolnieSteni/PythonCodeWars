def square_sum(numbers):
    sum1 = sum(list(map(lambda  x: pow(x,2), numbers)))
    return sum1
print(square_sum([1,2]))