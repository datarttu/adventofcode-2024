from adventofcode_2024 import day_02


def test_safe_report():
    assert day_02.is_report_safe("7 6 4 2 1")


def test_unsafe_nonmonotonic():
    assert not day_02.is_report_safe("1 3 2 4 5")


def test_unsafe_large_step():
    assert not day_02.is_report_safe("1 2 7 8 9")


def test_unsafe_zero_step():
    assert not day_02.is_report_safe("8 6 4 4 1")
