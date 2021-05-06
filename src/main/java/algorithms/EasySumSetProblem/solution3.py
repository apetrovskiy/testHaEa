'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted
# data to output will cause the test cases to fail
'''

# Write your code here
from typing import List, Set


def calculate_b(list_a: List[int], list_c: List[int]) -> Set[str]:
    # result_list = [list_c[0] - list_a[0]]
    # for index_c in range(1, len(list_c)):
    #     # print(index_c)
    #     # print(f"candidates are {[a + b for a
    # in list_a for b in result_list]}")
    #     # print(f"not in? {list_c[index_c] not
    # in [a + b for a in list_a for b in result_list]}")
    #     if list_c[index_c] not in [a + b for a
    # in list_a for b in result_list]:
    #         for index_a in range(len(list_a)):
    #             candidate = list_c[index_c] - list_a[index_a]
    #             result_list.append(candidate)
    #             break
    #         # candidate = min([a for a in list_a if list_c[index_c] > a])
    #         # print(f"candidate = {candidate}")
    #         # result_list.append(candidate)
    #         # for index_a in range(len(list_a)):
    #         #     candidate = list_c[index_c] - list_a[index_a]
    #         #     if candidate in result_list:
    #         #         continue
    #         #     else:
    #         #         result_list.append(candidate)
    #         #         break
    # result_list.sort()
    # return set([str(x) for x in result_list])
    result_list = []
    for index_c in range(1, len(list_c)):
        # print(index_c)
        # print(f"candidates are {[a + b for a
        # in list_a for b in result_list]}")
        # print(f"not in? {list_c[index_c] not
        # in [a + b for a in list_a for b in result_list]}")
        # if list_c[index_c] not in [a + b for a
        # in list_a for b in result_list]:
        for index_a in range(len(list_a)):
            if list_c[index_c] > list_a[index_a]:
                candidate = list_c[index_c] - list_a[index_a]
                result_list.append(candidate)
                break
            else:
                # candidate = list_c[index_c] - list_a[index_a + 1]
                continue
            # candidate = list_c[index_c] - list_a[index_a]
            # result_list.append(candidate)
            # break
            # candidate = min([a for a in list_a if list_c[index_c] > a])
            # print(f"candidate = {candidate}")
            # result_list.append(candidate)
            # for index_a in range(len(list_a)):
            #     candidate = list_c[index_c] - list_a[index_a]
            #     if candidate in result_list:
            #         continue
            #     else:
            #         result_list.append(candidate)
            #         break
    result_list.sort()
    return set([str(x) for x in result_list])


# length_of_a = int(input())
# list_a = [int(x) for x in input().split(' ')]
# length_of_c = int(input())
# list_c = [int(x) for x in input().split(' ')]
# result = calculate_b(list_a, list_c)
# print(' '.join(result))
