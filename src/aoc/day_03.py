from typing import TextIO


def part_01(input: TextIO) -> int:
    def parse_line(line: str) -> int:
        total = 0
        for i in range(len(line)):
            if not line[0 + i : 4 + i] == "mul(":
                continue

            # 15 is arbitrary for max length of a mul segment
            next_comma = line[i : i + 15].find(",")
            if next_comma == -1:
                continue

            next_bracket = line[i : i + 15].find(")")
            if next_bracket == -1:
                continue

            try:
                x, y = line[i + 4 : i + next_bracket].split(",")
                total += int(x) * int(y)
            except:
                continue

        return total

    return parse_line("".join([line.strip() for line in input.readlines()]))


def part_02(input: TextIO) -> int:

    def parse_line(line: str) -> int:
        total = 0
        activated = True
        for i in range(len(line)):
            if line[i: i + 5] == "don't":
                activated = False
                # print(i, " Dectivated")
                continue

            if line [i: i + 2] == "do":
                activated = True
                # print(i, " Activated")
                continue

            if not activated:
                continue

            if not line[i : i + 4] == "mul(":
                continue

            # 15 is arbitrary for max length of a mul segment
            next_comma = line[i : i + 15].find(",")
            if next_comma == -1:
                continue

            next_bracket = line[i : i + 15].find(")")
            if next_bracket == -1:
                continue

            try:
                x, y = line[i + 4 : i + next_bracket].split(",")
                total += int(x) * int(y)
            except:
                continue

        return total

    return parse_line("".join([line.strip() for line in input.readlines()]))
