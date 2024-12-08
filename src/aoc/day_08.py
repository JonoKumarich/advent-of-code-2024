from collections import defaultdict
from copy import deepcopy
from itertools import combinations
from typing import TextIO


def part_01(input: TextIO) -> int:
    antennas = defaultdict(set)
    lines = [list(line.strip()) for line in input.readlines()]
    width = len(lines[0])
    height = len(lines)

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '.':
                continue
            antennas[char].add((x, y))

    antinodes = set()
    viz = defaultdict(set)
    for key, locations in antennas.items():
        pairs = list(combinations(locations, 2))

        for a, b in pairs:
            distance = (b[0] - a[0], b[1] - a[1])

            antinode_a = (a[0] - distance[0], a[1] - distance[1])
            antinode_b = (b[0] + distance[0], b[1] + distance[1])

            if 0 <= antinode_a[0] < height and 0 <= antinode_a[1] < width:
                antinodes.add(antinode_a)
                viz[key].add(antinode_a)

            if 0 <= antinode_b[0] < height and 0 <= antinode_b[1] < width:
                antinodes.add(antinode_b)
                viz[key].add(antinode_b)

    # for key, values in viz.items():
    #     print('\n key: ', key)
    #     grid = deepcopy(lines)
    #     for (x, y) in values:
    #         grid[y][x] = '#'
    #
    #     for line in grid:
    #         print(''.join(line))


    return len(antinodes)


def part_02(input: TextIO) -> int:
    pass
