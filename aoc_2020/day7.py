import re
from typing import Tuple, List, Dict


def parse_line(line: str) -> Tuple[str, Dict[str, int]]:
    primary_re = re.compile(r"(\w+ \w+) bags contain")
    others_re = re.compile(r"(\d) (\w+ \w+) bags?")

    p_match = primary_re.match(line)
    if p_match is not None:
        primary = p_match.groups()[0]

        o_match = others_re.findall(line)
        
        res = {}
        for num, bag in o_match:
            res[bag] = int(num)

        return (primary, res)
    return ("", {})


def parse_data(data: str) -> Dict[str, Dict[str, int]]:

    res = {}
    for line in data.splitlines():
        if line != "":
            bag, contents = parse_line(line)
            res[bag] = contents

    return res


def contains_bag_type(all_contents: Dict[str, Dict[str, int]], search_type: str, bag_type: str) -> bool:
    contents = all_contents[search_type]

    if bag_type in contents:
        return True

    for bag in contents.keys():
        if contains_bag_type(all_contents, bag, bag_type):
            return True

    return False


def count_bag_type(all_contents: Dict[str, Dict[str, int]], bag_type: str) -> int:
    total = 0
    contents = all_contents[bag_type]

    for bag, count in contents.items():
        total += count
        total += count_bag_type(all_contents, bag) * count

    return total


def part1(data: str) -> int:
    print("Running day 7 part 1")

    all_contents = parse_data(data)

    count = 0
    for bag in all_contents.keys():
        if contains_bag_type(all_contents, bag, "shiny gold"):
            count += 1

    print(count)
    return count


def part2(data: str) -> int:
    print("Running day 7 part 2")

    all_contents = parse_data(data)

    count = count_bag_type(all_contents, "shiny gold")

    print(count)
    return count