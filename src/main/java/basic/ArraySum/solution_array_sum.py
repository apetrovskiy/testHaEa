'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data
# to output will cause the test cases to fail
'''

# Write your code here
from typing import List


def solution_array_sum(input_array: List[int]) -> int:
    return sum(input_array)


'''
array_length = int(input())
array = [int(x) for x in input().split(' ')]
print(solution_array_sum(array))
'''
