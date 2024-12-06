from aocd import data, submit
import math, re, itertools, functools, collections, string, dataclasses

lines = data.splitlines()

def part1() -> int:
    muls = re.findall(r"mul\((\d+),(\d+)\)", data)
    return sum(int(a) * int(b) for a, b in muls)

def part2() -> int:
    total = 0
    for r in re.split(r"don't\(\).*?($|do\(\))", data, flags=re.DOTALL):
        muls = re.findall(r"mul\((\d+),(\d+)\)", r)
        total += sum(int(a) * int(b) for a, b in muls)
    return total


if __name__ == "__main__":
    print(f"Part 1: {(p1:=part1())}")
    submit(p1, part="a")
    print(f"Part 2: {(p2:=part2())}")
    submit(p2, part="b")