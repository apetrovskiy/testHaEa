from src.main.java.algorithms.EasySumSetProblem.solution3 import calculate_b
import pytest
from typing import List


test_data = [
    ([1, 2], [3, 4, 5], ['2', '3']),
    ([3], [5, 6], ['2', '3']),
    ([4, 3, 5, 1], [3, 5, 6, 7, 8, 9], ['2', '4']),
    ([1, 3, 2, 5, 4], [2, 3, 4, 5, 6], ['1'])
]


@pytest.mark.parametrize("array_a,array_c,array_b", test_data)
def test_easy_sum_set(array_a: List[int], array_c: List[int], array_b: List[str]):
    print(f"expected = {array_b}")
    print(f"actual = {calculate_b(array_a, array_c)}")
    assert len(array_b) == len(calculate_b(array_a, array_c))
    assert all([a == b for a, b in zip(
        array_b, calculate_b(array_a, array_c))])
