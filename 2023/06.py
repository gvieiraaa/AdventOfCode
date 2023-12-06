from aocd import data, submit
import math, re, itertools, functools, collections, string, dataclasses


def part1() -> int:
    lines = [line.split()[1:] for line in data.splitlines()]
    races = [tuple([int(x), int(y)]) for x, y in zip(*lines)]
    product = 1
    for race in races:
        product *= sum(1 for i in range(1, race[0]) if (race[0] - i) * i > race[1])
    return product


def part2() -> int:
    time, distance = data.splitlines()
    time = int(time.replace(" ", "").partition(":")[2])
    distance = int(distance.replace(" ", "").partition(":")[2])
    return sum(1 for i in range(1, time) if (time - i) * i > distance)


if __name__ == "__main__":
    print(f"Part 1: {(p1:=part1())}")
    submit(p1, part="a")
    print(f"Part 2: {(p2:=part2())}")
    submit(p2, part="b")