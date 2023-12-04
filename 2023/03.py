from aocd import data, submit
import math, re, itertools, functools, collections, string, copy

def get_neightbors_index(list_: list[str], x: int, y: int):
    min_x = max(0, x-1)
    max_x = min(len(list_)-1, x+1)
    min_y = max(0, y-1)
    max_y = min(len(list_[0])-1, y+1)
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            if not (x==i and y==j):
                yield (i, j)


def part1(data: str) -> int:
    lines = data.splitlines()

    sum_numbers = 0
    for i, line in enumerate(lines):
        #print(line)
        for match_re in re.finditer(r"\d+", line):
            print(int(line[match_re.span()[0]:match_re.span()[1]]))
            if any(
                lines[x][y] in "*-+$&=@/#%"
                for n in range(*match_re.span())
                for x, y in get_neightbors_index(lines, i, n)
            ):
                sum_numbers += int(line[match_re.span()[0]:match_re.span()[1]])
    return sum_numbers

def part2(data: str) -> int:
    inputlines = data.splitlines()
    r_length = len(inputlines)
    c_length = len(inputlines[0])
    ratios = []

    for r_index,row in enumerate(inputlines):
        for c_index, char in enumerate(row):
            if char == '*':
                parts = []
                for r_offset in range(-1,2):
                    for c_offset in range(-1,2):
                        r,c = r_index+r_offset,c_index+c_offset
                        if r < 0 or c < 0:
                            continue
                        if r >= r_length or c >= c_length:
                            continue
                        if inputlines[r][c].isdigit():
                            part = inputlines[r][c]
                            p_index = (r,c)
                            for offset in [1,2]:
                                if inputlines[r][c-offset].isdigit():
                                    part = inputlines[r][c-offset] + part
                                    p_index = (r,c-offset)
                                else:
                                    break
                            for offset in [1,2]:
                                if inputlines[r][c+offset].isdigit():
                                    part = part + inputlines[r][c+offset]
                                else:
                                    break
                            part = (int(part),p_index)
                            if part not in parts: parts.append(part)
                if len(parts) == 2:
                    ratios.append(parts[0][0] * parts[1][0])

    return sum(ratios)
    

if __name__ == '__main__':
    print(f"Part 1: {(p1:=part1(data))}")
    submit(p1, part="a")
    print(f"Part 2: {(p2:=part2(data))}")
    submit(p2, part="b")