from aoc_2020.day7 import parse_line, parse_data, part1, part2

data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

data2="""shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

def test_parse_line():
    contents = parse_line("light red bags contain 1 bright white bag, 2 muted yellow bags")
    assert contents == ("light red", {"bright white": 1, "muted yellow": 2} )


def test_parse_data():
    parsed = parse_data(data)
    assert parsed["light red"] == {"bright white": 1, "muted yellow": 2}
    assert parsed["bright white"] == {"shiny gold": 1}
    assert parsed["dotted black"] == {}


def test_part1():
    assert part1(data) == 4


def test_part2():
    assert part2(data2) == 126