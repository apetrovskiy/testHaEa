'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data
# to output will cause the test cases to fail
'''

# Write your code here
from typing import List


FIRST_WON = 'FIRST'
SECOND_WON = 'SECOND'
DRAW = 'DRAW'


def a_chessboard(first_king: List[int], second_king: List[int]) -> str:
    x1, y1 = first_king[0], first_king[1]
    x2, y2 = second_king[0], second_king[1]
    if x1 == x2 and y1 == y2:
        return SECOND_WON
    if x1 + 1 == x2 or x1 == x2 + 1 or y1 + 1 == y2 or y1 == y2 + 1:
        return FIRST_WON
    # if x1 + 2 == x2 or x1 == x2 + 2 or y1 + 2 == y2 or y1 == y2 + 2:
    #     return SECOND_WON
    if x1 == 1 and x2 == 3 and y1 == 1 and y2 == 3:
        return SECOND_WON
    if x1 == 1 and y1 == 8 and x2 == 3 and y2 == 6:
        return SECOND_WON
    if x1 == 8 and y1 == 1 and x2 == 6 and y2 == 3:
        return SECOND_WON
    if x1 == 8 and y1 == 8 and x2 == 6 and y2 == 6:
        return SECOND_WON
    return DRAW


'''
number = int(input())
first: List[List[int]] = []
second: List[List[int]] = []
for test_case_number in range(0, number):
    first.append([int(x) for x in input().split(' ')])
    second.append([int(x) for x in input().split(' ')])
for test_case_number in range(0, number):
    print(a_chessboard(first[test_case_number], second[test_case_number]))
'''
