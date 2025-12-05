from utils.file_reader import read_input

YEAR = 2025
DAY = 2


def is_invalid_id(id: int) -> bool:
    id_string = str(id)
    id_string_len = len(id_string)
    if id_string_len % 2 == 0:
        mid = id_string_len // 2
        start = id_string[mid:]
        end = id_string[:mid]

        return start == end

    return False


def part1(data: list[str]) -> int:
    sum_up_invalid_ids = 0
    ids_ranges = data[0].split(",")

    for id_range in ids_ranges:
        [start, end] = id_range.split("-")
        numbers_from_range = list(range(int(start), int(end) + 1))
        invalid_ids = filter(lambda n: is_invalid_id(n), numbers_from_range)
        sum_up_invalid_ids += sum(list(invalid_ids))

    return sum_up_invalid_ids


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
