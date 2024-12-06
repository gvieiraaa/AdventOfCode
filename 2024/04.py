from aocd import data, submit
import math, re, itertools, functools, collections, string, dataclasses

data2 = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

lines = data.splitlines()

def part1() -> int:
    matrix = [list(line) for line in lines]
    directions = list(itertools.product((-1, 0, 1), (-1, 0, 1)))
    directions.remove((0, 0))
    total = 0
    max_row = len(matrix)
    max_column = len(matrix[0])
    for start_row, start_column in itertools.product(range(max_row), range(max_column)):
        for x, y in directions:
            text = matrix[start_row][start_column]
            for i in range(1, 4):
                i_row = start_row + i * x
                i_column = start_column + i * y
                if any([i_row < 0, i_row > max_row - 1, i_column < 0, i_column > max_column - 1]):
                    break
                text += matrix[i_row][i_column]
            if text == "XMAS":
                total += 1
        
    return total

def part2() -> int:
    matrix = [list(line) for line in lines]
    total = 0
    max_row = len(matrix)
    max_column = len(matrix[0])
    for start_row, start_column in itertools.product(range(max_row - 2), range(max_column - 2)):
        results = [
            "".join(matrix[start_row + i_row][start_column + i_column] for i_row, i_column in coords)
            for coords in (((0, 0), (1, 1), (2, 2)), ((2, 2), (1, 1), (0, 0)), ((2, 0), (1, 1), (0, 2)), ((0, 2), (1, 1), (2, 0)))
        ]
        if results.count("MAS") == 2:
            total += 1

    return total


if __name__ == "__main__":
    print(f"Part 1: {(p1:=part1())}")
    submit(p1, part="a")
    print(f"Part 2: {(p2:=part2())}")
    submit(p2, part="b")