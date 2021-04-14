'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted
# data to output will cause the test cases to fail
'''

# Write your code here
from typing import List


def providing_gifts(number: int, cases: List[int]) -> List[int]:
    result: List[int] = []
    for index in range(0, number):
        number_of_coins: int = cases[index]
        sum_of_coins: int = number_of_coins * (number_of_coins + 1) // 2
        preliminary_result: int = int(sum_of_coins / number_of_coins)
        result.append(preliminary_result)
    return result


# number_of_cases: int = int(input())
# cases: List[int] = []
# for i in (range(number_of_cases)):
#     cases.append(int(input()))
# result: List[int] = providing_gifts(number_of_cases, cases)
# [print(x) for x in result]
