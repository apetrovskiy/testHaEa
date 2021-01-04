from src.main.java.basic.ArraySum.solution3 import solution_array_sum
import pytest
from typing import List


test_data = [
    ([1000000001, 1000000002, 1000000003, 1000000004, 1000000005], 5000000015),
    ([1001458909, 1004570889, 1007019111, 1003302837, 1002514638,
      1006431461, 1002575010, 1007514041, 1007548981, 1004402249], 11)
]


@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_array_sum(input_array: List[int], expected_result: int):
    assert expected_result == solution_array_sum(input_array)
