from collections import defaultdict
def part_01(input: list[str]) -> int:

    a, b = zip(*[line.split() for line in input])

    return sum([abs(int(x) - int(y)) for (x, y) in zip(sorted(a), sorted(b))])



def part_02(input: list[str]) -> int:
    a, b = zip(*[line.split() for line in input])

    occurances = defaultdict(lambda: 0)

    for char in b:
        occurances[int(char)] += 1

    return sum(int(char) * occurances[int(char)] for char in a)








