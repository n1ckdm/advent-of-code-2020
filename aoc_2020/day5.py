from math import ceil
from typing import Tuple, List

Vec2 = Tuple[int, int]


def get_pos(code: str) -> Vec2:
    rmin = 0
    rmax = 127
    cmin = 0
    cmax = 7
    for c in code:
        rdiff = rmax - rmin
        cdiff = cmax - cmin
        if c == "F":
            rmax = rmin + rdiff // 2
        elif c == "B":
            rmin = rmin + ceil(rdiff / 2)
        elif c == "L":
            cmax = cmin + cdiff // 2
        else:
            cmin = cmin + ceil(cdiff / 2)
    
    return (rmin, cmin)


def get_seats(codes: List[str]) -> List[Vec2]:
    seats = []
    for code in codes:
        seats.append(
            get_pos(code)
        )
    return seats


def part1(data: str) -> int:
    print("Running day 5 part 1")

    seats = get_seats(data.splitlines())
    max_id = max([s[0]*8 + s[1] for s in seats])
    print(max_id)
    return max_id
