'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from typing import List


def calculate_item(c: int, list_a: List[int]) -> str:
    index = 0
    b = -1
    while b < 0:
        if c > list_a[index]:
            return str(c - list_a[index])
    return '0'


def calculate_b(list_a: List[int], list_c: List[int]) -> List[str]:
    return set([calculate_item(c, list_a) for c in list_c])


length_of_a = int(input())
list_a = [int(x) for x in input().split(' ')]
length_of_c = int(input())
list_c = [int(x) for x in input().split(' ')]
result = calculate_b(list_a, list_c)
print(' '.join(result))
