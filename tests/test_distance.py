import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app import calculate_distance


def test_distance_simple():
    result = calculate_distance([2, 5], [1, 6])

    assert round(result, 3) == 1.414


def test_distance_nulle():
    result = calculate_distance([2, 5], [2, 5])

    assert result == 0


def test_distance_negative():
    result = calculate_distance([-1, -2], [3, 4])

    assert round(result, 3) == 7.211


def test_distance_decimal():
    result = calculate_distance([1.5, 2.5], [3.5, 4.5])

    assert round(result, 3) == 2.828