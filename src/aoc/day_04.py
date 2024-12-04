from typing import TextIO
from itertools import product


# def part_01(input: TextIO) -> int:
#     lines = [list(line.strip()) for line in input.readlines()]
#     n_rows = len(lines)
#     n_cols = len(lines[0])
#     n_diagonals = n_rows + n_cols -1
#
#     total = 0
#
#     for x in range(n_rows):
#         row = lines[x]
#         total += row.count("XMAS")
#         total += row.count("SAMX")
#
#     for y in range(n_cols):
#         column = "".join([line[y] for line in lines])
#         total += column.count("XMAS")
#         total += column.count("SAMX")
#
#     for n in range(n_diagonals):
#         values = []
#         for i in range(min(n, n_rows)):
#
#
#     return total


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

        if m < n_rows - 3  and n < n_cols - 3:
            neg_diagonal = [lines[m + i][n + i] for i in range(4)]
            if neg_diagonal in XMAS:
                total += 1

        if m < n_rows - 3  and n < n_cols - 3:
            rev_lines = [list(reversed(line)) for line in lines]
            pos_diagonal = [rev_lines[m + i][n + i] for i in range(4)]
            if pos_diagonal in XMAS:
                total += 1

    return total

def part_02(input: TextIO) -> int:
    raise NotImplementedError
