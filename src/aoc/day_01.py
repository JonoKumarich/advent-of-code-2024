from collections import defaultdict
from typing import TextIO


def part_01(input: TextIO) -> int:
    a, b = zip(*[line.split() for line in input.readlines()])

    return sum([abs(int(x) - int(y)) for (x, y) in zip(sorted(a), sorted(b))])


def part_02(input: TextIO) -> int:
    a, b = zip(*[line.split() for line in input.readlines()])

    occurances = defaultdict(lambda: 0)

    for char in b:
        occurances[int(char)] += 1

    return sum(int(char) * occurances[int(char)] for char in a)
