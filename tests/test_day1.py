import aoc_2020


def test_part1():
    result = aoc_2020.day1.part1(aoc_2020.inputs.day1.data)
    assert (result[0] + result[1]) == 2020


def test_part2():
    result = aoc_2020.day1.part2(aoc_2020.inputs.day1.data)
    assert (result[0] + result[1] + result[2]) == 2020
