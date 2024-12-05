from collections import defaultdict
from typing import TextIO


def part_01(input: TextIO) -> int:
    rules, manuals = map(lambda x: x.split(), input.read().split("\n\n"))

    rules = [list(map(int, rule.split("|"))) for rule in rules]
    manuals = [list(map(int, manual.split(","))) for manual in manuals]

    next_rules = defaultdict(set)
    prev_rules = defaultdict(set)
    for rule in rules:
        next_rules[rule[0]].add(rule[1])
        prev_rules[rule[1]].add(rule[0])

    total = 0
    for manual in manuals:
        orders = {rule: n for n, rule in enumerate(manual)}
        valid = True

        for key, constraints in next_rules.items():
            if key not in orders:
                continue

            for constraint in constraints:
                if constraint not in orders:
                    continue

                if orders[key] < orders[constraint]:
                    continue

                valid = False
                break

            if not valid:
                break

        for key, constraints in prev_rules.items():
            if key not in orders:
                continue

            for constraint in constraints:
                if constraint not in orders:
                    continue

                if orders[key] > orders[constraint]:
                    continue

                valid = False
                break

            if not valid:
                break

        if valid:
            total += manual[int(len(manual) / 2)]

    return total


def part_02(input: TextIO) -> int:
    raise NotImplementedError
