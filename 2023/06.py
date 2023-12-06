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
    time = int(time.replace(" ", "").split(":")[1])
    distance = int(distance.replace(" ", "").split(":")[1])
    # for i in range(time):
    #     if (time - i) * i > distance:
    #         return(time - i*2 + time%2)
    d = time**2 - 4*distance
    r1 = (time + d**0.5) / 2
    r2 = (time - d**0.5) / 2
    return (time - 2 * math.ceil(min(x for x in (r1, r2) if x > 0)) + time%2)


if __name__ == "__main__":
    print(f"Part 1: {(p1:=part1())}")
    submit(p1, part="a")
    print(f"Part 2: {(p2:=part2())}")
    submit(p2, part="b")