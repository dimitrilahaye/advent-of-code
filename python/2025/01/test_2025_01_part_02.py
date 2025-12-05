import pytest
from solution_01 import part2


def test_to_right_one_targeting_dial_during_rotation():
    # Arrange
    data: list[str] = [
        "R51",
    ]

    # Act
    result = part2(data)

    # Assert
    assert result == 1


def test_to_right_one_targeting_from_52_starting_point_dial_during_rotation():
    # Arrange
    data: list[str] = [
        "R30",
    ]

    # Act
    result = part2(data, 52)

    # Assert
    assert result == 0


def test_to_right_two_targeting_dial_during_rotation():
    # Arrange
    data: list[str] = [
        "R151",
    ]

    # Act
    result = part2(data)

    # Assert
    assert result == 2


def test_to_left_9_targeting_dial_from_0_starting_point_during_rotation():
    # Arrange
    data: list[str] = [
        "L348",
    ]

    # Act
    result = part2(data, 0)

    # Assert
    assert result == 3


def test_to_right_10_targeting_dial_during_rotation():
    # Arrange
    data: list[str] = [
        "R1000",
    ]

    # Act
    result = part2(data)

    # Assert
    assert result == 10


def test_to_left_one_targeting_dial_during_rotation():
    # Arrange
    data: list[str] = [
        "L50",
    ]

    # Act
    result = part2(data)

    # Assert
    assert result == 1


def test_to_left_one_targeting_dial_from_82_starting_point_during_rotation():
    # Arrange
    data: list[str] = [
        "L30",
    ]

    # Act
    result = part2(data, 82)

    # Assert
    assert result == 0


def test_to_left_one_targeting_dial_from_0_starting_point_during_rotation():
    # Arrange
    data: list[str] = [
        "L5",
    ]

    # Act
    result = part2(data, 0)

    # Assert
    assert result == 0


def test_to_left_two_targeting_dial_during_rotation():
    # Arrange
    data: list[str] = [
        "L151",
    ]

    # Act
    result = part2(data)

    # Assert
    assert result == 2


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
    result = part2(data)

    # Assert
    assert result == 6
