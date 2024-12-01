from aocd import data, submit
import math, re, itertools, functools, collections, string, dataclasses

lines = data.splitlines()

def part1() -> int:
    n1 = []
    n2 = []
    for line in lines:
        a, b = line.split()
        n1.append(int(a))
        n2.append(int(b))
    
    n1.sort()
    n2.sort()

    total = sum(abs(x - y) for x, y in zip(n1, n2))

    return total

def part2() -> int:
    n1 = []
    n2 = []
    for line in lines:
        a, b = line.split()
        n1.append(int(a))
        n2.append(int(b))
    
    total = sum(number * n2.count(number) for number in n1)

    return total


if __name__ == "__main__":
    print(f"Part 1: {(p1:=part1())}")
    submit(p1, part="a")
    print(f"Part 2: {(p2:=part2())}")
    submit(p2, part="b")