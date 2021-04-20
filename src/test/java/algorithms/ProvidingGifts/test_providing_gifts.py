from src.main.java.algorithms.ProvidingGifts.providing_gifts \
    import providing_gifts
from typing import List
import pytest


test_data = [
    (1, [4], [2]),
    (10, [4, 5, 6, 7, 8, 9, 10, 11, 15, 20], [2, 3, 3, 4, 5, 5, 6, 6, 7, 7]),
    (10, [7747, 1995, 523, 6067, 3105, 3654, 7692, 1545, 2447, 6040, 7423,
          7690, 3641, 3753, 5474, 1520, 8846, 9862, 8037, 5691, 1092, 3137,
          7921, 4782, 2305, 8159, 5918, 127, 3795, 6233, 6219, 9163,
          4954, 3756, 1498, 3535, 473, 1481, 8256, 1584, 3928, 2181, 5562],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
]


@pytest.mark.parametrize("number,cases,expected_result", test_data)
def test_providing_gifts(number: int,
                         cases: List[int], expected_result: List[int]):
    assert expected_result == providing_gifts(number, cases)
