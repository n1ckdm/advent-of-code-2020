from aoc_2020.day2 import parse_line, part1, part2


def test_parse_line():
    assert parse_line("1-3 a: abcde") == (1, 3, "a", "abcde")


def test_part1():
    data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    assert part1(data) == 2


def test_part2():
    data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    assert part2(data) == 1
