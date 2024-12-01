from pathlib import Path


def split_to_ints(line: str) -> list[int]:
    items = line.strip().split("   ")
    int_items = [int(item) for item in items]
    return int_items


def main(input_file: Path) -> None:
    with open(input_file, "r") as f:
        pairs = [split_to_ints(line) for line in f.readlines()]
    s1, s2 = (sorted(lst) for lst in zip(*pairs))
    sum_of_diffs = sum(abs(i1 - i2) for i1, i2 in zip(s1, s2))
    print(sum_of_diffs)


if __name__ == "__main__":
    main(Path("inputs/day_01.txt"))