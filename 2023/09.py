from aocd import data, submit
import math, re, itertools, functools, collections, string, dataclasses

lines = data.splitlines()

def part1() -> int:
    lines = [list(map(int, line.split())) for line in data.splitlines()]
    sum_all = 0
    for line in lines:
        sequences = [line]
        while any(sequences[-1]):
            sequences.append([x - y for x, y in zip(sequences[-1][1:], sequences[-1][:-1])])
        while len(sequences) != 1:
            last = sequences.pop()
            sequences[-1][-1] += last[-1]
        sum_all += sequences[0][-1]
    return sum_all

def part2() -> int:
    lines = [list(map(int, line.split())) for line in data.splitlines()]
    sum_all = 0
    for line in lines:
        sequences = [line]
        while any(sequences[-1]):
            sequences.append([x - y for x, y in zip(sequences[-1][1:], sequences[-1][:-1])])
        while len(sequences) != 1:
            first = sequences.pop()
            sequences[-1][0] -= first[0]
        sum_all += sequences[0][0]
    return sum_all


if __name__ == "__main__":
    print(f"Part 1: {(p1:=part1())}")
    submit(p1, part="a")
    print(f"Part 2: {(p2:=part2())}")
    submit(p2, part="b")