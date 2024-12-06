from aocd import data, submit
import math, re, itertools, functools, collections, string, dataclasses

data2 = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

lines = data.splitlines()

def turn(direction):
    return [direction[1], - direction[0]]

def part1() -> int:
    matrix = [list(line) for line in lines]
    visited = set()
    for ix, x in enumerate(matrix):
        for iy, y in enumerate(x):
            if y == "^":
                pos = (ix, iy)
                matrix[ix][iy] == "."
    direction = [-1, 0]
    while True:
        visited.add(pos)
        max_row = len(matrix) - 1
        max_column = len(matrix[0]) - 1
        if not (0 <= pos[0] + direction[0] <= max_row and 0 <= pos[1] + direction[1] <= max_column):
            break
        looking = matrix[pos[0] + direction[0]][pos[1] + direction[1]]
        if looking == "#":
            direction = turn(direction)
        else:
            pos = (pos[0] + direction[0], pos[1] + direction[1])


    return len(visited)

def part2() -> int:
    matrix = [list(line) for line in lines]
    visited = set()
    for ix, x in enumerate(matrix):
        for iy, y in enumerate(x):
            if y == "^":
                pos = (ix, iy)
                matrix[ix][iy] == "."
    direction = [-1, 0]
    while True:
        visited.add(pos)
        max_row = len(matrix) - 1
        max_column = len(matrix[0]) - 1
        if not (0 <= pos[0] + direction[0] <= max_row and 0 <= pos[1] + direction[1] <= max_column):
            break
        looking = matrix[pos[0] + direction[0]][pos[1] + direction[1]]
        if looking == "#":
            direction = turn(direction)
        else:
            pos = (pos[0] + direction[0], pos[1] + direction[1])

    total = 0

    for a, b in visited:
        matrix = [list(line) for line in lines]
        matrix[a][b] = "#"
        visited2 = set()
        for ix, x in enumerate(matrix):
            for iy, y in enumerate(x):
                if y == "^":
                    pos = (ix, iy)
                    matrix[ix][iy] == "."
        direction = [-1, 0]
        for _ in range(10_000):
            visited2.add(pos)
            max_row = len(matrix) - 1
            max_column = len(matrix[0]) - 1
            if not (0 <= pos[0] + direction[0] <= max_row and 0 <= pos[1] + direction[1] <= max_column):
                break
            looking = matrix[pos[0] + direction[0]][pos[1] + direction[1]]
            if looking == "#":
                direction = turn(direction)
            else:
                pos = (pos[0] + direction[0], pos[1] + direction[1])
        else:
            total += 1

    return total


if __name__ == "__main__":
    print(f"Part 1: {(p1:=part1())}")
    #submit(p1, part="a")
    print(f"Part 2: {(p2:=part2())}")
    submit(p2, part="b")