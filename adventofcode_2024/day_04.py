from typing import Sequence


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]


def match_in_directions(puzzle: Sequence[str], word: str, row: int, col: int) -> int:
    delta = len(word)
    frame = [line[col : col + delta] for line in puzzle[row : row + delta]]
    candidates = (
        frame[0],
        "".join(line[0] for line in frame),
        "".join(line[i] for i, line in enumerate(frame)),
        "".join(line[-i - 1] for i, line in enumerate(frame)),
    )
    return sum(c.count(word) + c.count(word[::-1]) for c in candidates)


def xmas_count(raw_puzzle: Sequence[str]) -> int:
    word = "XMAS"
    buffer = len(word) - 1
    collen = len(raw_puzzle[0]) + buffer
    puzzle = [line.strip() + ("." * buffer) for line in raw_puzzle] + [
        "." * collen
    ] * buffer

    res = 0
    for row in range(len(raw_puzzle)):
        for col in range(len(raw_puzzle[0])):
            res += match_in_directions(puzzle, word, row, col)
    return res


def mas_in_x(puzzle: Sequence[str], row: int, col: int) -> int:
    frame = [line[col : col + 3] for line in puzzle[row : row + 3]]

    candidates = (
        "".join(frame[i][i] for i in range(3)),
        "".join(frame[i][-i - 1] for i in range(3)),
    )
    return all(candidate in ("MAS", "SAM") for candidate in candidates)


def mas_count(puzzle: Sequence[str]) -> int:
    res = 0
    for row in range(len(puzzle) - 2):
        for col in range(len(puzzle[0]) - 2):
            res += int(mas_in_x(puzzle, row, col))
    return res


def main():
    p = read_lines("inputs/day_04.txt")
    print("Part 1:", xmas_count(p))
    print("Part 2:", mas_count(p))


if __name__ == "__main__":
    main()
