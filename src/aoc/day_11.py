from functools import lru_cache
from typing import TextIO


def part_01(input: TextIO) -> int:
    stones = map(int, input.read().strip().split())

    total = 0
    for stone in stones:
        total += blink_stone(stone, 25)

    return total

@lru_cache
def blink_stone(stone: int, n_times: int) -> int:
    print(stone, n_times)
    if n_times == 0:
        return 1

    if stone == 0:
        return blink_stone(1, n_times - 1)

    elif (stone_len := len(str(stone))) % 2 == 0:
        return blink_stone(
            int(str(stone)[: int(stone_len / 2)]), n_times - 1
        ) + blink_stone(int(str(stone)[int(stone_len / 2) :]), n_times - 1)
    else:
        return blink_stone(stone * 2024, n_times - 1)


def part_02(input: TextIO) -> int:
    stones = map(int, input.read().strip().split())

    total = 0
    for stone in stones:
        total += blink_stone(stone, 25)

    return total
