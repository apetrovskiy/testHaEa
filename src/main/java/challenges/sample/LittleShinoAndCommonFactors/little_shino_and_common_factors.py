'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted
# data to output will cause the test cases to fail
'''

# Write your code here


def little_shino_and_common_factors(number1, number2):
    result = len([i for i, j in zip(get_factors(
        number1), get_factors(number2)) if i == j])
    print(result)
    return result


def get_factors(number):
    factors = [0] if number == 0 else [1]
    while number % 2 == 0:
        factors.append(2)
        number = int(number / 2)

    divisor = 3
    while number % divisor == 0:
        factors.append(divisor)
        number = int(number / divisor)
        divisor += 1

    if number > 1:
        factors.append(number)
    return factors


# input_data = [int(x) for x in list(input().split(' '))]
# little_shino_and_common_factors(input_data[0], input_data[1])
