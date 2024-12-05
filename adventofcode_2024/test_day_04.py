import pytest

from adventofcode_2024 import day_04


@pytest.fixture(scope="session")
def testdata():
    yield [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]


def test_xmas_count(testdata):
    assert day_04.xmas_count(testdata) == 18


def test_match_in_x(testdata):
    assert not day_04.mas_in_x(testdata, 0, 0)
    assert day_04.mas_in_x(testdata, 0, 1)
    assert not day_04.mas_in_x(testdata, 7, 7)


def test_mas_count(testdata):
    assert day_04.mas_count(testdata) == 9
