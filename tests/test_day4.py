import re
from aoc_2020.day4 import parse_data, get_next_passport, get_passport, part1


data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""


def test_get_next_pp():
    pp, new_data = get_next_passport(data.splitlines())
    assert (
        pp
        == "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
    )

    pp, new_data = get_next_passport(new_data)
    assert pp == "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929"

    pp, new_data = get_next_passport(new_data)
    assert (
        pp == "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm"
    )


def test_get_passport():
    res = get_passport(
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
    )
    assert res["ecl"] == "gry"


def test_data_parse():
    res = parse_data(data)
    assert res[0]["ecl"] == "gry"


def test_part1():
    assert part1(data) == 2


def test_hair_regex():
    assert re.fullmatch("#[0-9a-f]{6}", "#123abc") is not None
    assert re.fullmatch("#[0-9a-f]{6}", "#123abz") is None
