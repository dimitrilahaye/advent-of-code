import pytest
import os
from solution_0 import part2

BASE_DIR = os.path.dirname(__file__)


def test_part1():
    # Arrange
    data: list[str] = ["1", "2"]

    # Act
    result = part2(data)

    # Assert
    assert result == 2
