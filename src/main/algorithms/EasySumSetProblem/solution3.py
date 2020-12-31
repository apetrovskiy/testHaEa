'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from typing import List, Set


# def calculate_item(c: int, list_a: List[int]) -> str:
#     index = 0
#     b = -1
#     while b < 0:
#         if c > list_a[index]:
#             return str(c - list_a[index])
#     return '0'


def calculate_b(list_a: List[int], list_c: List[int]) -> Set[str]:
    # return set([calculate_item(c, list_a) for c in list_c])
    result_list = []
    print(len(list_c))
    for index_c in range(len(list_c)):
        for index_a in range(len(list_a)):
            candidate = list_c[index_c] - list_a[index_a]
            if candidate in result_list:
                continue
            else:
                result_list.append(candidate)
                break
    return set([str(x) for x in result_list])


# length_of_a = int(input())
# list_a = [int(x) for x in input().split(' ')]
# length_of_c = int(input())
# list_c = [int(x) for x in input().split(' ')]
# result = calculate_b(list_a, list_c)
# print(' '.join(result))
