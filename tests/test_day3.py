from aoc_2020.day3 import move, part1

data = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]


def test_move_output():
    assert move((0, 0), (1, 0), data) == ("#", (1, 0))
    assert move((0, 0), (1, 1), data) == (".", (1, 1))
    assert move((0, 0), (11, 0), data) == (None, None)
    assert move((0, 0), (1, 11), data) == ("#", (1, 0))


def test_part1():
    assert part1(data) == 7
