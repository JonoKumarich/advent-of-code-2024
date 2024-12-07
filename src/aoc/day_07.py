from typing import TextIO
from itertools import product


def part_01(input: TextIO) -> int:
    tests = [line.split(": ") for line in input.readlines()]
    tests = [(int(test[0]), list(map(int, test[1].split()))) for test in tests]

    total_correct = 0
    for res, eq in tests:
        configurations = product("*+", repeat=len(eq) - 1)
        for configuration in configurations:
            total = eq[0]
            for n, num in enumerate(eq[1:]):
                match configuration[n]:
                    case "*":
                        total *= num
                    case "+":
                        total += num
                    case _:
                        raise ValueError


            if total == res:
                total_correct += res
                break

    return total_correct


def part_02(input: TextIO) -> int:
    tests = [line.split(": ") for line in input.readlines()]
    tests = [(int(test[0]), list(map(int, test[1].split()))) for test in tests]

    total_correct = 0
    for n, (res, eq) in enumerate(tests):
        configurations = product("*+|", repeat=len(eq) - 1)
        for configuration in configurations:
            total = eq[0]
            for n, num in enumerate(eq[1:]):
                match configuration[n]:
                    case "*":
                        total *= num
                    case "+":
                        total += num
                    case "|":
                        total = int(str(total) + str(num))
                    case _:
                        raise ValueError

            if total == res:
                total_correct += res
                break

    return total_correct
