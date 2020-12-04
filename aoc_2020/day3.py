from functools import reduce
from typing import List, Tuple

Vec2 = Tuple[int, int]


def move(cur_pos: Vec2, mv: Vec2, grid: List[str]) -> str:
    if cur_pos[0] + mv[0] >= len(grid):
        return None, None

    row = cur_pos[0] + mv[0]
    col = cur_pos[1] + mv[1]

    width = len(grid[0])
    if col >= width:
        col = col - width

    return grid[row][col], (row, col)


def get_trees(data: List[str], slope: Vec2 = (1, 3)) -> int:
    pos = (0, 0)
    res, pos = move(pos, slope, data)
    trees = 0
    while res is not None:
        if res == "#":
            trees += 1
        res, pos = move(pos, slope, data)

    return trees


def part1(data: List[str]):
    print("Running day 3 part 1")

    trees = get_trees(data)
    print(trees)
    return trees


def part2(data: List[str]):
    print("Running day 3 part 2")

    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

    trees = []
    for slope in slopes:
        trees.append(get_trees(data, slope))

    res = reduce(lambda x, y: x * y, trees)
    print(res)
    return res
