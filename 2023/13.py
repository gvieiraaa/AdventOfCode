from aocd import data, submit
import math, re, itertools, functools, collections, string, dataclasses

def transpose(data):
    lines = data.splitlines()
    transposed = ["".join(row) for row in zip(*lines)]
    return "\n".join(transposed)

def get_diff(d1: list, d2: list) -> int:
    counter = 0
    for n1, n2 in zip(d1, d2):
        counter += sum(1 for char1, char2 in zip(n1, n2) if char1 != char2)
    return counter

def part1() -> int:
    total = 0
    for each in re.split(r"\n\n", data):
        lines = each.splitlines()
        for i in range(1, len(lines)):
            left = lines[:i]
            right = lines[i:]
            size = min(len(left), len(right))
            left_adjusted = lines[i - size:i]
            right_adjusted = lines[i:i + size]
            right_adjusted.reverse()
            if left_adjusted == right_adjusted:
                total += 100 * i
                break

        lines = transpose(each).splitlines()
        for i in range(1, len(lines)):
            left = lines[:i]
            right = lines[i:]
            size = min(len(left), len(right))
            left_adjusted = lines[i - size:i]
            right_adjusted = lines[i:i + size]
            right_adjusted.reverse()
            if left_adjusted == right_adjusted:
                total += i
                break

    return total

def part2() -> int:
    total = 0
    for each in re.split(r"\n\n", data):
        lines = each.splitlines()
        for i in range(1, len(lines)):
            left = lines[:i]
            right = lines[i:]
            size = min(len(left), len(right))
            left_adjusted = lines[i - size:i]
            right_adjusted = lines[i:i + size]
            right_adjusted.reverse()
            if get_diff(left_adjusted, right_adjusted) == 1:
                total += 100 * i
                break

        lines = transpose(each).splitlines()
        for i in range(1, len(lines)):
            left = lines[:i]
            right = lines[i:]
            size = min(len(left), len(right))
            left_adjusted = lines[i - size:i]
            right_adjusted = lines[i:i + size]
            right_adjusted.reverse()
            if get_diff(left_adjusted, right_adjusted) == 1:
                total += i
                break

    return total


if __name__ == "__main__":
    print(f"Part 1: {(p1:=part1())}")
    submit(p1, part="a")
    print(f"Part 2: {(p2:=part2())}")
    submit(p2, part="b")