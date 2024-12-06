from aocd import data, submit
import math, re, itertools, functools, collections, string, dataclasses

data2 = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

lines = data.splitlines()

def part1() -> int:
    counter = 0
    for line in lines:
        d = list(map(int, line.split()))
        if (d == sorted(d) or d == list(reversed(sorted(d)))) and all(1 <= abs(a - b) <= 3 for a, b in zip(d[:-1], d[1:])):
            counter += 1
    return counter

def part2() -> int:
    counter = 0
    for line in lines:
        d = list(map(int, line.split()))
        for i in range(len(d)):
            copy = d.copy()
            copy.pop(i)
            if (copy == sorted(copy) or copy == list(reversed(sorted(copy)))) and all(1 <= abs(a - b) <= 3 for a, b in zip(copy[:-1], copy[1:])):
                counter += 1
                break
    return counter


if __name__ == "__main__":
    print(f"Part 1: {(p1:=part1())}")
    submit(p1, part="a")
    print(f"Part 2: {(p2:=part2())}")
    submit(p2, part="b")