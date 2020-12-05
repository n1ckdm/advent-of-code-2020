from aoc_2020.day5 import part1, get_pos, part2

data = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
"""


def test_get_pos():
    assert get_pos("FBFBBFFRLR") == (44, 5)


def test_part1():
    assert part1(data) == 820


def test_part2():
    assert part2(data) is None
