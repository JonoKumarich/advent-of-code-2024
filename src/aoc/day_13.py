from typing import TextIO


def part_01(input: TextIO) -> int:
    games = [game.split("\n") for game in input.read().split("\n\n")]
    total = 0
    for game in games:
        a1 = int(game[0].split()[2][2:-1])
        a2 = int(game[0].split()[3][2:])
        b1 = int(game[1].split()[2][2:-1])
        b2 = int(game[1].split()[3][2:])
        c1 = -int(game[2].split()[1][2:-1])
        c2 = -int(game[2].split()[2][2:])

        x = (b1 * c2 - b2 * c1) / (b2 * a1 - b1 * a2)
        y = (c1 * a2 - c2 * a1) / (b2 * a1 - b1 * a2)

        if x != float(int(x)) or y != float(int(y)):
            continue

        if x > 100 or y > 100:
            continue

        total += 3 * x + y

    return int(total)

