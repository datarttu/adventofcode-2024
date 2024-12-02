def is_report_safe(report: str) -> bool:
    levels = [int(level) for level in report.split(" ")]
    differences = [levels[i] - levels[i + 1] for i in range(len(levels) - 1)]
    return all(d >= 1 and d <= 3 for d in differences) or all(
        d >= -3 and d <= -1 for d in differences
    )


def count_safe_reports(input_file: str) -> int:
    with open(input_file, "r") as f:
        reports = f.readlines()
    return len([r for r in reports if is_report_safe(r)])


def main():
    print(count_safe_reports("inputs/day_02.txt"))


if __name__ == "__main__":
    main()
