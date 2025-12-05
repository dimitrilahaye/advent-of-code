import pytest
import os
from solution import part1, part2

BASE_DIR = os.path.dirname(__file__)


def test_to_right_zero_targeting_dial():
    # Arrange
    data: list[str] = [
        "R1",
    ]

    # Act
    result = part1(data)

    # Assert
    assert result == 0


def test_to_right_one_targeting_dial():
    # Arrange
    data: list[str] = ["R1", "R49"]

    # Act
    result = part1(data)

    # Assert
    assert result == 1


def test_to_left_zero_targeting_dial():
    # Arrange
    data: list[str] = [
        "L1",
    ]

    # Act
    result = part1(data)

    # Assert
    assert result == 0


def test_to_left_one_targeting_dial():
    # Arrange
    data: list[str] = ["L1", "L49"]

    # Act
    result = part1(data)

    # Assert
    assert result == 1


def test():
    # Arrange
    data: list[str] = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]

    # Act
    result = part1(data)

    # Assert
    assert result == 3


@pytest.mark.skip()
def test_part2():
    # Arrange
    data: list[str] = ["1", "2"]

    # Act
    result = part2(data)

    # Assert
    assert result == 2
