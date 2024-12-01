def split_to_ints(line: str) -> list[int]:
    items = line.strip().split("   ")
    int_items = [int(item) for item in items]
    return int_items


def sum_of_diffs(input_data: str) -> int:
    pairs = [split_to_ints(line) for line in input_data.split("\n")]
    s1, s2 = (sorted(lst) for lst in zip(*pairs))
    return sum(abs(i1 - i2) for i1, i2 in zip(s1, s2))


def similarity_score(input_data: str) -> int:
    l1, l2 = zip(*(split_to_ints(line) for line in input_data.split("\n")))
    return sum(item * l2.count(item) for item in l1)


if __name__ == "__main__":
    with open("inputs/day_01.txt", "r") as f:
        input_data = f.read()
    print(sum_of_diffs(input_data))
    print(similarity_score(input_data))
