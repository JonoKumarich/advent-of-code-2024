from typing import TextIO


def part_01(input: TextIO) -> int:
    lines = [line.strip() for line in input.readlines()]
    n_rows = len(lines)
    n_cols = len(lines[0])
    n_diagonals = max(n_rows, n_cols)

    total = 0

    for x in range(n_rows):
        row = lines[x]
        total += row.count("XMAS")
        total += row.count("SAMX")

    for y in range(n_cols):
        column = "".join([line[y] for line in lines])
        total += column.count("XMAS")
        total += column.count("SAMX")

    return total




def part_02(input: TextIO) -> int:
    raise NotImplementedError
