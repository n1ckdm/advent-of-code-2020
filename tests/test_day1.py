import aoc_2020

def test_part_1():
    result = aoc_2020.day1.run(aoc_2020.inputs.day1.data)
    assert (result[0] + result[1]) == 2020