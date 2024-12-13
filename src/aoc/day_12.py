from typing import TextIO
from itertools import product


def part_01(input: TextIO) -> int:
    grid = [list(line.strip()) for line in input.readlines()]

    visited = set()
    total = 0
    for m, n in product(range(len(grid)), range(len(grid[0]))):
        if (m, n) in visited:
            continue
        visited.add((m, n))
        neighbours = find_all_neighbours(grid, (m, n))
        visited.update(neighbours)
        area = len(neighbours)
        perimiter = calculate_perimiter(grid, neighbours)
        total += area * perimiter

    return total


def calculate_perimiter(grid: list[list[str]], locations: set[tuple[int, int]]) -> int:
    perimiter = 0
    for location in locations:
        neighbours = find_direct_neighbours(grid, location)
        perimiter += 4 - len(neighbours)

    return perimiter


def find_all_neighbours(
    grid: list[list[str]],
    current: tuple[int, int],
) -> set[tuple[int, int]]:
    to_search = find_direct_neighbours(grid, current)
    visited = set()
    visited.add(current)

    while len(to_search) > 0:
        next_loc = to_search.pop()
        visited.add(next_loc)
        neighbours = {
            n for n in find_direct_neighbours(grid, next_loc) if n not in visited
        }
        to_search.update(neighbours)

    return visited


def find_direct_neighbours(
    grid: list[list[str]],
    current: tuple[int, int],
) -> set[tuple[int, int]]:
    neighbours = set()
    value = grid[current[0]][current[1]]

    if current[0] > 0 and grid[current[0] - 1][current[1]] == value:
        neighbours.add((current[0] - 1, current[1]))

    if current[1] > 0 and grid[current[0]][current[1] - 1] == value:
        neighbours.add((current[0], current[1] - 1))

    if current[0] < len(grid) - 1 and grid[current[0] + 1][current[1]] == value:
        neighbours.add((current[0] + 1, current[1]))

    if current[1] < len(grid[0]) - 1 and grid[current[0]][current[1] + 1] == value:
        neighbours.add((current[0], current[1] + 1))

    return neighbours

def part_02(input: TextIO) -> int:
    grid = [list(line.strip()) for line in input.readlines()]

    visited = set()
    total = 0
    for m, n in product(range(len(grid)), range(len(grid[0]))):
        if (m, n) in visited:
            continue
        visited.add((m, n))
        neighbours = find_all_neighbours(grid, (m, n))
        visited.update(neighbours)
        area = len(neighbours)
        perimiter = calculate_perimiter(grid, neighbours)
        total += area * perimiter

    return total

def calculate_num_sides(grid: list[list[str]], segment: set[tuple[int, int]]) -> int:
    # Calculate num sides of outer edge
    # Find all blocks inside of shape
    # Calculate num sides for each of those blocks
    pass
