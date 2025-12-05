from utils.file_reader import read_input
import math

YEAR = 2025
DAY = 1


def part1(data: list[str]) -> int:
    MAX_STEP = 100
    STARTING_STEP = 50
    target_count = 0
    current_position = STARTING_STEP

    for dial in data:
        direction = dial[0]
        steps = int(dial[1:])
        if direction == "L":
            current_position = (current_position - steps) % MAX_STEP

        if direction == "R":
            current_position = (current_position + steps) % MAX_STEP

        if current_position == 0:
            target_count += 1

    return target_count


def part2(data: list[str]) -> int:
    return data.__len__()


def solve():
    input_data = read_input(DAY, YEAR)
    answer_part1 = part1(input_data)
    answer_part2 = part2(input_data)
    print(f"--- Advent of Code {YEAR} - Jour {DAY:02d} ---")
    print(f"Partie 1: {answer_part1}")
    print(f"Partie 2: {answer_part2}")


if __name__ == "__main__":
    solve()
