from src.main.java.challenges.sample.LittleShinoAndCommonFactors.little_shino_and_common_factors import little_shino_and_common_factors
from typing import List
import pytest


test_data = [
    (10, 15, 2),
    (4, 8, 3),
    (0, 0, 1),
    (1, 1, 1),
    (2, 2, 2)
]


@pytest.mark.parametrize("number1,number2,expected_result", test_data)
def test_find_factors_version01(number1: int, number2: int, expected_result: List[int]):
    assert expected_result == little_shino_and_common_factors(number1, number2)
