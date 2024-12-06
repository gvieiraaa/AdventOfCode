from aocd import data, submit
import math, re, itertools, functools, collections, string, dataclasses
import copy

data = """\
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

lines = data.splitlines()

def part1() -> int:
    matrix = [[*line] for line in lines]
    matrix.append(["." for _ in range(len(matrix[0]))])
    print(matrix)
    while True:
        new = copy.deepcopy(matrix)
        for lower, upper in zip(new[1:], matrix[:-1]):
            print(lower, upper)
            row = []
            for l, u in zip(lower, upper):
                match l, u:
                    case _, "#":
                        row.append("#")
                    case _, "O":
                        row.append("O")
                    case ".", "O":
                        row.append("")
            break
        break


    return None

def part2() -> int:
    return None


if __name__ == "__main__":
    print(f"Part 1: {(p1:=part1())}")
    #submit(p1, part="a")
    #print(f"Part 2: {(p2:=part2())}")
    #submit(p2, part="b")