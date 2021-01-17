from src.main.java.challenges.competitive.JanuaryCircuits21.a01AChessboard.a_chessboard import a_chessboard
from typing import List
import pytest


test_data = [
    ([[[1, 1], [2, 2]], [[1, 3], [8, 8]]], ['FIRST', 'DRAW']),
    ([[[1, 1], [1, 1]]], ['SECOND'])
]


@pytest.mark.parametrize("input_data,expected_result", test_data)
def test_a_chessboard(input_data: List[List[int]], expected_result: List[str]):
    for test_case_number in range(0, len(input_data)):
        assert expected_result[test_case_number] == a_chessboard(
            input_data[test_case_number][0], input_data[test_case_number][1])
