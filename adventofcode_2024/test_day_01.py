import pytest

from adventofcode_2024 import day_01


@pytest.fixture(scope="session", autouse=True)
def testdata() -> str:
    return "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"


def test_part_1(testdata):
    assert day_01.sum_of_diffs(testdata) == 11


def test_part_2(testdata):
    assert day_01.similarity_score(testdata) == 31
