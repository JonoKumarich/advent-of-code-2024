from itertools import pairwise

def diff_parser(report: list[str]) -> bool:

    diffs = [int(y)-int(x) for (x, y) in pairwise(report)]

    max_diff = max(diffs)
    min_diff = min(diffs)

    total_max_diff = max(abs(max_diff), abs(min_diff))

    if max_diff == 0 or min_diff == 0:
        return False

    if max_diff > 0 and min_diff < 0:
        return False

    if total_max_diff > 3:
        return False

    return True

def part_01(input: list[str]) -> int:

    total = 0
    for report in input:
        if diff_parser(report.split()):
            total += 1

    return total


# Very inefficient - but works quickly given small input
def part_02(input: list[str]) -> int:
    total = 0
    for report in input:
        levels = report.split()
        for n in range(len(levels)):
            tmp = levels.copy()
            del tmp[n]
            if diff_parser(tmp):
                total += 1
                break

    return total
