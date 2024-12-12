from collections import Counter, defaultdict
from functools import lru_cache
from typing import TextIO


def part_01(input: TextIO) -> int:
    stones = list(map(int, input.read().strip().split()))
    return blink_many(stones, 25)

def part_02(input: TextIO) -> int:
    stones = list(map(int, input.read().strip().split()))
    return blink_many(stones, 75)

def blink_many(stones: list[int], n: int) -> int:
    stone_freq = Counter(stones)

    for _ in range(n):
        new = defaultdict(lambda: 0)
        for stone, n in stone_freq.items():
            for s in blink_once(stone):
                new[s] += n

        stone_freq = new

    return sum(stone_freq.values())

@lru_cache
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
