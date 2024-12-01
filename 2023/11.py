from aocd import data, submit
import math, re, itertools, functools, collections, string, dataclasses

data2 = """\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

lines = data.splitlines()

def part1() -> int:
    empty_rows = []
    empty_columns = []
    for iline, line in enumerate(lines):
        if all(s=="." for s in line):   
            empty_rows.append(iline)

    matrix = [list(line) for line in lines]
    width = len(matrix[0])

    for i in range(width):
        if all(matrix[x][i] == "." for x in range(len(matrix))):
            empty_columns.append(i)

    all_positions = []
    for ix, x in enumerate(matrix):
        for iy, y in enumerate(x):
            if y == "#":
                all_positions.append([ix, iy])

    print(empty_rows)
    print(empty_columns)

    total_distance = 0
    multiplier = 1
    for (x1, y1), (x2, y2) in itertools.combinations(all_positions, r=2):
        empty_rows_between = sum(1 for x in empty_rows if min(x1, x2) < x < max(x1, x2))
        empty_columns_between = sum(1 for x in empty_columns if min(y1, y2) < x < max(y1, y2))
        total_distance += abs(x1 - x2)
        total_distance += abs(y1 - y2)
        total_distance += empty_rows_between * multiplier
        total_distance += empty_columns_between * multiplier

    return total_distance

def part2() -> int:
    empty_rows = []
    empty_columns = []
    for iline, line in enumerate(lines):
        if all(s=="." for s in line):   
            empty_rows.append(iline)

    matrix = [list(line) for line in lines]
    width = len(matrix[0])

    for i in range(width):
        if all(matrix[x][i] == "." for x in range(len(matrix))):
            empty_columns.append(i)

    all_positions = []
    for ix, x in enumerate(matrix):
        for iy, y in enumerate(x):
            if y == "#":
                all_positions.append([ix, iy])

    total_distance = 0
    multiplier = 1_000_000 - 1
    for (x1, y1), (x2, y2) in itertools.combinations(all_positions, r=2):
        empty_rows_between = sum(1 for x in empty_rows if min(x1, x2) < x < max(x1, x2))
        empty_columns_between = sum(1 for x in empty_columns if min(y1, y2) < x < max(y1, y2))
        total_distance += abs(x1 - x2)
        total_distance += abs(y1 - y2)
        total_distance += empty_rows_between * multiplier
        total_distance += empty_columns_between * multiplier

    return total_distance


if __name__ == "__main__":
    print(f"Part 1: {(p1:=part1())}")
    submit(p1, part="a")
    print(f"Part 2: {(p2:=part2())}")
    submit(p2, part="b")