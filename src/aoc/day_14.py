from collections import defaultdict
from typing import TextIO

WIDTH = 101
HEIGHT = 103
NUM_ITERS = 100

WIDTH_MID = int(WIDTH / 2)
HEIGHT_MID = int(HEIGHT / 2)


def part_01(input: TextIO) -> int:
    robots = [
        list(map(lambda x: x, line.strip().split())) for line in input.readlines()
    ]
    robots = [(robot[0][2:].split(","), robot[1][2:].split(",")) for robot in robots]
    locations = []

    for start, dir in robots:
        current = list(map(int, start))
        dir = tuple(map(int, dir))

        for _ in range(NUM_ITERS):
            current[0] = (current[0] + dir[0]) % WIDTH
            current[1] = (current[1] + dir[1]) % HEIGHT

        locations.append(current)

    a = 0
    b = 0
    c = 0
    d = 0

    for loc in locations:
        if loc[0] < WIDTH_MID and loc[1] < HEIGHT_MID:
            a += 1
        elif loc[0] < WIDTH_MID and loc[1] > HEIGHT_MID:
            b += 1
        elif loc[0] > WIDTH_MID and loc[1] < HEIGHT_MID:
            c += 1
        elif loc[0] > WIDTH_MID and loc[1] > HEIGHT_MID:
            d += 1

    return a * b * c * d
