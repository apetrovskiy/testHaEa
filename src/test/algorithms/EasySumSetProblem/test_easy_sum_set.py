import pytest
from typing import List
from src.main.algorithms.EasySumSetProblem.solution3 import calculate_b


test_data = [
    ([1, 2], [3, 4, 5], ['2', '3'])
]


@pytest.mark.parametrize("array_a,array_c,array_b", test_data)
def test_easy_sum_set(array_a: List[int], array_c: List[int], array_b: List[str]):
    assert array_b == calculate_b(array_a, array_c)
