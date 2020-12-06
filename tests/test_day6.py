from aoc_2020.day6 import parse_group, parse_data, part1, part2

data = """abc

a
b
c

ab
ac

a
a
a
a

b
"""


def test_parse_group():
    assert parse_group("abc") == {"a": 1, "b": 1, "c": 1}
    assert parse_group("aaaaaa") == {"a": 6}


def test_parse_data():
    assert parse_data(data) == [
        ({"a": 1, "b": 1, "c": 1}, 1),
        ({"a": 1, "b": 1, "c": 1}, 3),
        ({"a": 2, "b": 1, "c": 1}, 2),
        ({"a": 4}, 4),
        ({"b": 1}, 1),
    ]


def test_part1():
    assert part1(data) == 11


def test_part2():
    assert part2(data) == 6
