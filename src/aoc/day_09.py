from collections import namedtuple
from typing import TextIO
from tqdm import tqdm


def part_01(input: TextIO) -> int:
    sequence = []

    for n, char in enumerate(input.read().strip()):
        sequence.extend([int(n / 2) if n % 2 == 0 else None for _ in range(int(char))])

    num_nulls = sequence.count(None)

    for n, val in enumerate(reversed(sequence)):
        if n >= num_nulls:
            break

        if val is None:
            continue

        sequence[sequence.index(None)] = val
        sequence[len(sequence) - n - 1] = None

    total = 0
    for i, num in enumerate(sequence):
        if num is None:
            break
        total += i * num

    return total


Block = namedtuple("Block", ["size", "index"])


def part_02(input: TextIO) -> int:
    sequence = []
    for n, char in enumerate(input.read().strip()):
        if n % 2 == 0:
            sequence.append(Block(int(char), int(n / 2)))
        else:
            sequence.append(Block(int(char), None))

    for block in tqdm(list(reversed(sequence))):
        if block.index is None:
            continue

        for match in sequence:
            n = list(reversed(sequence)).index(block)
            i = sequence.index(match)
            if match.index is not None or match.size == 0:
                continue

            if match.size < block.size:
                continue

            if i >= len(sequence) - n - 1:
                break

            new_blocks = repartition_block(match, block)
            sequence = sequence[:i] + new_blocks + sequence[i + 1 :]
            ix_to_pop = len(sequence) - n - 1
            sequence[ix_to_pop] = Block(block.size, None)
            break

    total = 0
    index = 0
    for block in sequence:
        if block.index is None:
            index += block.size
            continue
        for _ in range(block.size):
            total += block.index * index
            index += 1

    return total


def print_blocks(blocks: list[Block]) -> str:
    output = ""
    for block in blocks:
        for _ in range(block.size):
            output += str(block.index) if block.index is not None else "."
    print(output)
    return output


def repartition_block(current: Block, incoming: Block) -> list[Block]:
    assert incoming.index is not None
    if current.size == incoming.size:
        return [incoming]

    extra = Block(current.size - incoming.size, None)
    return [incoming, extra]

    # (2, 9)
    # (3, None)
