from collections import defaultdict
from itertools import combinations
from typing import TextIO


def antenna_locations(grid: list[list[str]]) -> dict[str, set[tuple[int, int]]]:
    antennas = defaultdict(set)
    for x, line in enumerate(grid):
        for y, char in enumerate(line):
            if char == ".":
                continue
            antennas[char].add((x, y))

    return antennas


def part_01(input: TextIO) -> int:
    lines = [list(line.strip()) for line in input.readlines()]
    width = len(lines[0])
    height = len(lines)
    antennas = antenna_locations(lines)

    antinodes = set()
    for locations in antennas.values():
        pairs = list(combinations(locations, 2))

        for a, b in pairs:
            distance = (b[0] - a[0], b[1] - a[1])

            antinode_a = (a[0] - distance[0], a[1] - distance[1])
            antinode_b = (b[0] + distance[0], b[1] + distance[1])

            if 0 <= antinode_a[0] < height and 0 <= antinode_a[1] < width:
                antinodes.add(antinode_a)

            if 0 <= antinode_b[0] < height and 0 <= antinode_b[1] < width:
                antinodes.add(antinode_b)

    return len(antinodes)


def part_02(input: TextIO) -> int:
    lines = [list(line.strip()) for line in input.readlines()]
    width = len(lines[0])
    height = len(lines)
    antennas = antenna_locations(lines)
    antinodes = set()

    for locations in antennas.values():
        antinodes.union(locations)
        pairs = list(combinations(locations, 2))

        for a, b in pairs:
            distance = (b[0] - a[0], b[1] - a[1])

            # a ->
            n = 0
            while True:
                antinode = (a[0] - (n * distance[0]), a[1] - (n * distance[1]))
                if not (0 <= antinode[0] < height and 0 <= antinode[1] < width):
                    break
                antinodes.add(antinode)
                n += 1

            # b ->
            n = 0
            while True:
                antinode = (b[0] + (n * distance[0]), b[1] + (n * distance[1]))
                if not (0 <= antinode[0] < height and 0 <= antinode[1] < width):
                    break
                antinodes.add(antinode)
                n += 1

    return len(antinodes)
