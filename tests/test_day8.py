from aoc_2020.day8 import part1, part2

data = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""


def test_part1():
    assert part1(data) == (5, 0)


def test_part2():
    assert part2(data) == (8, 1)
