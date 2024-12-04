from typing import TextIO
import re


def part_01(input: TextIO) -> int:
    values = re.findall(
        r"mul\((\d+),(\d+)\)",
        "".join([line.strip() for line in input.readlines()]),
    )
    assert values is not None
    return sum(map(lambda x: int(x[0]) * int(x[1]), values))


def part_02(input: TextIO) -> int:
    values = re.findall(
        r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)",
        "".join([line.strip() for line in input.readlines()]),
    )

    total = 0
    active = True
    for value in values:
        if value == "don't()":
            active = False
        elif value == "do()":
            active = True
        else:
            if not active:
                continue
            x, y = value[4:-1].split(",")
            total += int(x) * int(y)

    return total
