from src.main.java.challenges.sample.FredoAndArrayUpdate.\
    fredo_and_array_update import fredo_and_array_update
from typing import List
import pytest


test_data = [
    (5, [1, 2, 3, 4, 5], 4)
]


@pytest.mark.parametrize("number,data,expected_result", test_data)
def test_find_factors_version01(number: int,
                                data: List[int],
                                expected_result: List[int]):
    assert expected_result == fredo_and_array_update(number, data)
