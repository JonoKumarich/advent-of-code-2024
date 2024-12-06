from typing import TextIO
from itertools import product
from copy import deepcopy


def find_start(grid: list[list[str]]) -> tuple[int, int]:
    for n, row in enumerate(grid):
        row = "".join(row)
        loc = max(
            row.find("v"),
            row.find(">"),
            row.find("<"),
            row.find("^"),
        )
        if loc != -1:
            return (n, loc)

    raise ValueError("Start not found")


def part_01(input: TextIO) -> int:
    grid = [list(line.strip()) for line in input.readlines()]
    current = find_start(grid)
    col_size = len(grid)
    row_size = len(grid[0])

    direction = {
        "v": (1, 0),
        ">": (0, 1),
        "<": (0, -1),
        "^": (-1, 0),
    }[grid[current[0]][current[1]]]
    grid[current[0]][current[1]] = "."
    next_move = (current[0] + direction[0], current[1] + direction[1])

    next_direction = {
        (1, 0): (0, -1),
        (0, 1): (1, 0),
        (0, -1): (-1, 0),
        (-1, 0): (0, 1),
    }

    visited = set()
    visited.add(current)
    while True:
        if next_move[0] < 0 or next_move[0] >= col_size:
            break

        if next_move[1] < 0 or next_move[1] >= row_size:
            break

        value = grid[next_move[0]][next_move[1]]

        match value:
            case ".":
                visited.add(next_move)
                current = next_move
            case "#":
                direction = next_direction[direction]
            case _:
                raise ValueError("something went very wrong")

        next_move = (current[0] + direction[0], current[1] + direction[1])

    return len(visited)


def is_loop(grid: list[list[str]], current: tuple[int, int], direction: tuple[int, int]) -> bool:
    col_size = len(grid)
    row_size = len(grid[0])
    visited = set()
    visited.add((current, direction))
    next_move = (current[0] + direction[0], current[1] + direction[1])
    next_direction = {
        (1, 0): (0, -1),
        (0, 1): (1, 0),
        (0, -1): (-1, 0),
        (-1, 0): (0, 1),
    }

    while True:
        if next_move[0] < 0 or next_move[0] >= col_size:
            return False

        if next_move[1] < 0 or next_move[1] >= row_size:
            return False

        value = grid[next_move[0]][next_move[1]]

        match value:
            case ".":
                current = next_move
                if (current, direction) in visited:
                    return True

                visited.add((current, direction))
            case "#":
                direction = next_direction[direction]
            case _:
                raise ValueError("something went very wrong")

        next_move = (current[0] + direction[0], current[1] + direction[1])

def part_02(input: TextIO) -> int:
    grid = [list(line.strip()) for line in input.readlines()]
    current = find_start(grid)
    col_size = len(grid)
    row_size = len(grid[0])

    direction = {
        "v": (1, 0),
        ">": (0, 1),
        "<": (0, -1),
        "^": (-1, 0),
    }[grid[current[0]][current[1]]]
    grid[current[0]][current[1]] = "."

    loops = 0
    for r, c in  product(range(col_size), range(row_size)):
        if grid[r][c] == '.':
            new_grid = deepcopy(grid)
            new_grid[r][c] = '#'

            if is_loop(new_grid, current, direction):
                loops += 1

    return loops
