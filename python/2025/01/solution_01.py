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


def part2(data: list[str], starting_step=50) -> int:
    MAX_STEP = 100
    STARTING_STEP = starting_step
    target_count = 0
    current_position = STARTING_STEP
    new_step = 0

    for dial in data:
        direction = dial[0]
        steps = int(dial[1:])
        how_many_zeros = 0

        if direction == "L":
            new_step = current_position - steps

            if steps >= current_position:
                if current_position > 0:
                    how_many_zeros = 1
                    remaining_distance = steps - current_position
                elif current_position == 0:
                    remaining_distance = steps

                how_many_zeros += remaining_distance // MAX_STEP

        if direction == "R":
            new_step = current_position + steps

            if new_step == MAX_STEP:
                how_many_zeros = 1
            elif new_step > MAX_STEP:
                how_many_zeros = new_step // MAX_STEP

        target_count += how_many_zeros
        current_position = new_step % MAX_STEP

    return target_count


def solve():
    input_data = read_input(DAY, YEAR)
    answer_part1 = part1(input_data)
    answer_part2 = part2(input_data)
    print(f"--- Advent of Code {YEAR} - Jour {DAY:02d} ---")
    print(f"Partie 1: {answer_part1}")
    print(f"Partie 2: {answer_part2}")


if __name__ == "__main__":
    solve()
