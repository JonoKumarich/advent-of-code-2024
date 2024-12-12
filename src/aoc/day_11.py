# from collections import deque
from typing import TextIO


def part_01(input: TextIO) -> int:
    stones = list(map(int, input.read().strip().split()))

    for _ in range(25):
        stones = blink(stones)

    return len(stones)


def blink(stones: list[int]) -> list[int]:
    new_stones = stones.copy()
    i = 0
    for stone in stones:
        if stone == 0:
            new_stones[i] = 1
        elif (stone_len := len(str(stone))) % 2 == 0:
            new_stones.pop(i)
            new_stones.insert(i, int(str(stone)[: int(stone_len / 2)]))
            new_stones.insert(i + 1, int(str(stone)[int(stone_len / 2) :]))
            i += 1
        else:
            new_stones[i] = new_stones[i] * 2024

        i += 1

    return new_stones


def part_02(input: TextIO) -> int:
    pass
