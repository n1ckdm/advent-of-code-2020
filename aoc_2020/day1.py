from typing import List


def get_sum(arr: List[int], _sum: int):
    comp = set()
    for num in arr:
        rem = _sum - num
        if num in comp:
            return (num, rem)
        else:
            comp.add(rem)

    return None


def part1(data: List[int]):
    print("Running day 1 part 1")
    res = get_sum(data, 2020)
    print(res[0] * res[1])
    return res


def part2(data: List[int]):
    print("Running day 1 part 2")

    for num in data:
        rem = 2020 - num
        res = get_sum(data, rem)
        if res is not None:
            print(num * res[0] * res[1])
            return (num, res[0], res[1])

    return (0, 0, 0)
