import pytest
from solution_02 import is_invalid_id, part1


def test_is_invalid_id():
    assert is_invalid_id(11) == True
    assert is_invalid_id(22) == True
    assert is_invalid_id(1010) == True
    assert is_invalid_id(1188511885) == True
    assert is_invalid_id(1227775554) == False


def test_part_extreme_one_range():
    # Arrange
    data: list[str] = ["11-22"]

    # Act
    result = part1(data)

    # Assert
    assert result == 33


def test_part_extreme_two_ranges():
    # Arrange
    data: list[str] = ["11-22,1188511880-1188511890"]

    # Act
    result = part1(data)

    # Assert
    assert result == 1188511918
