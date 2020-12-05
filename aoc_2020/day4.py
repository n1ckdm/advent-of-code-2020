import re
from typing import Dict, Union, List, Tuple

Passport = Dict[str, Union[int, str]]


def get_next_passport(data: List[str]) -> Tuple[str, List[str]]:
    passport = ""
    ind = 0
    for line in data:
        ind += 1
        if line == "":
            break
        passport += f" {line}"

    return passport.strip(), data[ind:]


def get_passport(pp_str: str) -> Passport:
    pp: Passport = {}
    for field in pp_str.split(" "):
        key, value = field.split(":")
        pp[key] = int(value) if value.isdigit() and not key == "pid" else value
    return pp


def parse_data(data: str) -> List[Passport]:

    passports: List[Passport] = []
    passport, new_data = get_next_passport(data.splitlines())
    while len(passport) > 0:
        passports.append(get_passport(passport))
        passport, new_data = get_next_passport(new_data)

    return passports


def valid_height(height: str) -> bool:
    if "cm" in height:
        h = int(height.split("cm")[0])
        return h >= 150 and h <= 193
    elif "in" in height:
        h = int(height.split("in")[0])
        return h >= 59 and h <= 76
    else:
        return False


def passport_is_valid(pp: Passport, strict = False) -> bool:
    if len(pp.keys()) == 8 or (len(pp.keys()) == 7 and "cid" not in pp):
        if (strict):
            valid = True
            valid &= int(pp["byr"]) >= 1920 and int(pp["byr"]) <= 2002
            valid &= int(pp["iyr"]) >= 2010 and int(pp["iyr"]) <= 2020
            valid &= int(pp["eyr"]) >= 2020 and int(pp["eyr"]) <= 2030
            valid &= valid_height(str(pp["hgt"]))
            valid &= re.fullmatch("#[0-9a-f]{6}", str(pp["hcl"])) is not None
            valid &= pp["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl","oth"]
            valid &= str(pp["pid"]).isdigit() and len(str(pp["pid"])) == 9
            return valid
        else:
            return True
    return False


def part1(data: str) -> int:
    print("Running day 4 part 1")
    passports = parse_data(data)

    valids = 0
    for pp in passports:
        if passport_is_valid(pp):
            valids += 1

    print(valids)
    return valids


def part2(data: str) -> int:
    print("Running day 4 part 2")
    passports = parse_data(data)

    valids = 0
    for pp in passports:
        if passport_is_valid(pp, True):
            valids += 1

    print(valids)
    return valids
