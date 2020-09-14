#Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
#For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
#Note: The function accepts an integer and returns an integer


def square_digits(num):
    num_list = [int(c) for c in str(num)]
    sqrt_str = ""
    for i in num_list:
        sqrt_str += str(pow(i,2))
    return  int(sqrt_str)

square_digits(955)