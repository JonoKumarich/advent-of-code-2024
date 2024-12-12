from collections import Counter, defaultdict
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
    stones = Counter(map(int, input.read().strip().split()))

    for _ in range(75):
        new = defaultdict(lambda: 0)
        for stone, n in stones.items():
            for s in blink_once(stone):
                new[s] += n

        stones = new

    return sum(stones.values())

def blink_once(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    elif (stone_len := len(str(stone))) % 2 == 0:
        return [ 
            int(str(stone)[: int(stone_len / 2)]), 
            int(str(stone)[int(stone_len / 2) :])
        ]
    else:
        return [stone * 2024]
