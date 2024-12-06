from typing import TextIO


def find_start(grid: list[list[str]]) -> tuple[int, int]:
    for n, row in enumerate(grid):
        row = ''.join(row)
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
    grid = [list(line) for line in input.readlines()]
    current = find_start(grid)
    col_size = len(grid)
    row_size = len(grid[0])

    direction = {
        "v": (1, 0),
        ">": (0, 1),
        "<": (0, -1),
        "^": (-1, 0),
    }[grid[current[0]][current[1]]]
    grid[current[0]][current[1]] = '.'
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
            case '.':
                visited.add(next_move)
                current = next_move
            case '#':
                direction = next_direction[direction]
            case _:
                raise ValueError('something went very wrong')

        next_move = (current[0] + direction[0], current[1] + direction[1])


    return len(visited)



def part_02(input: TextIO) -> int:
    pass
