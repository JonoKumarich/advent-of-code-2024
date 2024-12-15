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
        corners = find_total_corners(neighbours)
        total += area * corners

    return total


def find_total_corners(
    possible: set[tuple[int, int]],
) -> int:
    corners = 0
    for square in possible:
        verticals = {(square[0] - 1, square[1]), (square[0], square[1] - 1)}
        diagonal = (square[0] - 1, square[1] - 1)
        corners += num_corners(possible, verticals, diagonal)

        verticals = {(square[0] - 1, square[1]), (square[0], square[1] + 1)}
        diagonal = (square[0] - 1, square[1] + 1)
        corners += num_corners(possible, verticals, diagonal)


        verticals = {(square[0] + 1, square[1]), (square[0], square[1] + 1)}
        diagonal = (square[0] + 1, square[1] + 1)
        corners += num_corners(possible, verticals, diagonal)

        verticals = {(square[0] + 1, square[1]), (square[0], square[1] - 1)}
        diagonal = (square[0] + 1, square[1] - 1)
        corners += num_corners(possible, verticals, diagonal)


    return corners


def num_corners(
    possible: set[tuple[int, int]],
    verticals: set[tuple[int, int]],
    diagonal: tuple[int, int],
) -> int:
    num_verticals = len(set(v for v in verticals if v in possible))

    if num_verticals == 0:
        return 1
    elif num_verticals == 2 and diagonal not in possible:
        return 1
    else:
        return 0
