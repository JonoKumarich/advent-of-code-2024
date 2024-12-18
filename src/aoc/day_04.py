from typing import TextIO
from itertools import product


def part_01(input: TextIO) -> int:
    lines = [list(line.strip()) for line in input.readlines()]
    n_rows = len(lines)
    n_cols = len(lines[0])

    XMAS = (["X", "M", "A", "S"], ["S", "A", "M", "X"])
    total = 0
    for m, n in product(range(n_rows), range(n_cols)):
        if n < n_cols - 3:
            horizontal = lines[m][n : n + 4]
            if horizontal in XMAS:
                total += 1

        if m < n_rows - 3:
            vertical = [line[n] for line in lines[m : m + 4]]
            if vertical in XMAS:
                total += 1

        if m < n_rows - 3 and n < n_cols - 3:
            neg_diagonal = [lines[m + i][n + i] for i in range(4)]
            if neg_diagonal in XMAS:
                total += 1

        if m < n_rows - 3 and n < n_cols - 3:
            rev_lines = [list(reversed(line)) for line in lines]
            pos_diagonal = [rev_lines[m + i][n + i] for i in range(4)]
            if pos_diagonal in XMAS:
                total += 1

    return total


def part_02(input: TextIO) -> int:
    lines = [list(line.strip()) for line in input.readlines()]
    n_rows = len(lines)
    n_cols = len(lines[0])

    XMAS = (["M", "A", "S"], ["S", "A", "M"])
    total = 0
    for m, n in product(range(1, n_rows - 1), range(1, n_cols - 1)):
        incr_diag = [lines[m - 1][n + 1], lines[m][n], lines[m + 1][n - 1]]
        decr_diag = [lines[m - 1][n - 1], lines[m][n], lines[m + 1][n + 1]]

        if incr_diag in XMAS and decr_diag in XMAS:
            total += 1

    return total
