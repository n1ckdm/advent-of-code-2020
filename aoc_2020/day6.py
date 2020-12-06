from typing import Dict, List, Tuple

Qs = Dict[str, int]
Result = Tuple[Qs, int]


def parse_group(group: str) -> Qs:
    qs = {}
    for c in set(group):
        qs[c] = group.count(c)
    return qs


def parse_data(data: str) -> List[Result]:
    res: List[Result] = []

    group = ""
    people = 0
    lines = data.splitlines()
    for i, line in enumerate(lines):
        if line == "":
            res.append((parse_group(group), people))
            group = ""
            people = 0
        elif i == len(lines) - 1:
            people += 1
            group += line.strip()
            res.append((parse_group(group), people))
        else:
            people += 1
            group += line.strip()

    return res


def part1(data: str) -> int:
    print("Running day 6 part 1")

    results = parse_data(data)
    answer = sum([len(qs.keys()) for qs, ppl in results])
    print(answer)
    return answer


def part2(data: str) -> int:
    print("Running day 6 part 2")

    results = parse_data(data)
    answer = 0
    for qs, ppl in results:
        for q, c in qs.items():
            if c == ppl:
                answer += 1

    print(answer)
    return answer
