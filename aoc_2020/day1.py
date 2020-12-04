from typing import List

def run(data: List[int]):
    print("Running day 1")

    comp = set()

    for num in data:
        rem = 2020 - num
        if num in comp:
            return (num, rem, rem*num)
        else:
            comp.add(rem)

    return (0, 0)