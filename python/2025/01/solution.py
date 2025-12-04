from utils.file_reader import read_input

YEAR = 2025
DAY = 1

def part1(data: list[str]) -> int:
    """Implémentation de la partie 1 du Jour 1."""
    return data.__len__()

def part2(data: list[str]) -> int:
    """Implémentation de la partie 2 du Jour 1."""
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