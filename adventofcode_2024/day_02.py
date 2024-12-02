def is_report_safe(report: str) -> bool:
    levels = [int(level) for level in report.split(" ")]
    differences = [levels[i] - levels[i + 1] for i in range(len(levels) - 1)]
    return all(d >= 1 and d <= 3 for d in differences) or all(
        d >= -3 and d <= -1 for d in differences
    )


def is_report_safe_tolerated(report: str) -> bool:
    if is_report_safe(report):
        return True
    levels = [int(level) for level in report.split(" ")]
    for i in range(len(levels)):
        tolerated_levels = levels[0:i] + levels[i + 1 :]
        differences = [
            tolerated_levels[i] - tolerated_levels[i + 1]
            for i in range(len(tolerated_levels) - 1)
        ]
        is_safe = all(d >= 1 and d <= 3 for d in differences) or all(
            d >= -3 and d <= -1 for d in differences
        )
        if is_safe:
            return True
    else:
        return False


def count_safe_reports(input_file: str) -> int:
    with open(input_file, "r") as f:
        reports = f.readlines()
    return len([r for r in reports if is_report_safe(r)])


def count_safe_reports_tolerated(input_file: str) -> int:
    with open(input_file, "r") as f:
        reports = f.readlines()
    return len([r for r in reports if is_report_safe_tolerated(r)])


def main():
    print(count_safe_reports("inputs/day_02.txt"))
    print(count_safe_reports_tolerated("inputs/day_02.txt"))


if __name__ == "__main__":
    main()
