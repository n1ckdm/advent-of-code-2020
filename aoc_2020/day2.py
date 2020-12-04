import re
from typing import List, Tuple


def parse_line(line: str) -> Tuple[int, int, str, str]:
    pattern = re.compile(r"(\d+)-(\d+) ([a-z]): (\w+)")

    res = re.findall(pattern, line)[0]
    rmin = int(res[0])
    rmax = int(res[1])

    return (rmin, rmax, res[2], res[3])


def part1(data: List[str]) -> int:
    print("Running day 2 part 1")

    valids = 0
    for line in data:
        rmin, rmax, char, pw = parse_line(line)

        c = pw.count(char)
        if c >= rmin and c <= rmax:
            valids += 1

    print(valids)
    return valids


def part2(data: List[str]) -> int:
    print("Running day 2 part 2")

    valids = 0
    for line in data:
        rmin, rmax, char, pw = parse_line(line)

        pos1 = pw[rmin - 1] == char
        pos2 = pw[rmax - 1] == char
        if (pos1 or pos2) and not (pos1 and pos2):
            valids += 1

    print(valids)
    return valids
