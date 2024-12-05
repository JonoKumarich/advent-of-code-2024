from collections import defaultdict
from typing import TextIO


def part_01(input: TextIO) -> int:
    rules, manuals = map(lambda x: x.split(), input.read().split("\n\n"))

    rules = [list(map(int, rule.split("|"))) for rule in rules]
    manuals = [list(map(int, manual.split(","))) for manual in manuals]

    flattened_rules = defaultdict(set)
    for rule in rules:
        flattened_rules[rule[0]].add(rule[1])

    total = 0
    for manual in manuals:
        orders = {rule: n for n, rule in enumerate(manual)}
        valid = True

        for key, constraints in flattened_rules.items():
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

        if valid:
            total += manual[int(len(manual) / 2)]

    return total

def order_manual_once(manual: list[int], flat_rules: dict[int, set[int]]) -> tuple[list[int], bool]:
    orders = {rule: n for n, rule in enumerate(manual)}

    for key, constraints in flat_rules.items():
        if key not in orders:
            continue

        for constraint in constraints:
            if constraint not in orders:
                continue

            key_index = orders[key]
            constraint_index = orders[constraint]

            if key_index < constraint_index: 
                continue

            # Move key page to one before constraint page
            manual.insert(constraint_index, manual.pop(key_index))
            return manual, False

    return manual, True



def part_02(input: TextIO) -> int:
    rules, manuals = map(lambda x: x.split(), input.read().split("\n\n"))

    rules = [list(map(int, rule.split("|"))) for rule in rules]
    manuals = [list(map(int, manual.split(","))) for manual in manuals]

    flattened_rules = defaultdict(set)
    for rule in rules:
        flattened_rules[rule[0]].add(rule[1])

    total = 0
    for manual in manuals:
        updated_manual = manual.copy()
        while True:
            updated_manual, completed = order_manual_once(updated_manual, flattened_rules)

            if completed:
                if updated_manual != manual:
                    total += updated_manual[int(len(manual) / 2)]
                break


    return total
