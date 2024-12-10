from typing import TextIO


def part_01(input: TextIO) -> int:
    grid = [list(map(int, line.strip())) for line in input.readlines()]

    total = 0
    for m, row in enumerate(grid):
        for n, start in enumerate(row):
            if start != 0:
                continue

            total += len(set(num_trailheads(grid, (m, n))))

    return total


def num_trailheads(
    grid: list[list[int]], current: tuple[int, int]
) -> list[tuple[int, int]]:
    options = []
    value = grid[current[0]][current[1]]
    if value == 9:
        return [current]

    if current[0] > 0:
        if grid[current[0] - 1][current[1]] == value + 1:
            options.append((current[0] - 1, current[1]))

    if current[1] > 0:
        if grid[current[0]][current[1] - 1] == value + 1:
            options.append((current[0], current[1] - 1))

    if current[0] < len(grid) - 1:
        if grid[current[0] + 1][current[1]] == value + 1:
            options.append((current[0] + 1, current[1]))

    if current[1] < len(grid[0]) - 1:
        if grid[current[0]][current[1] + 1] == value + 1:
            options.append((current[0], current[1] + 1))

    endpoints = []
    for option in options:
        endpoints.extend(num_trailheads(grid, option))

    return endpoints

def part_02(input: TextIO) -> int:
    grid = [list(map(int, line.strip())) for line in input.readlines()]

    total = 0
    for m, row in enumerate(grid):
        for n, start in enumerate(row):
            if start != 0:
                continue

            total += len(num_trailheads(grid, (m, n)))

    return total

