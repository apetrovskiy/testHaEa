'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or
# ill-formatted data to output will cause the test cases to fail
'''

# Write your code here


def fredo_and_array_update(number, data):
    result = 0
    array_sum = sum(data)
    array_new_sum = 0
    while array_new_sum <= array_sum:
        result += 1
        array_new_sum = number * result
    print(result)
    return result


# input_number = int(input())
# input_data = [int(x) for x in list(input().split(' '))]
# fredo_and_array_update(input_number, input_data)
