from aocd import data, submit, lines #, numbers

def part1():
    priority_sum = 0
    for line in lines:
        item1 = line[:len(line)//2]
        item2 = line[len(line)//2:]
        intersect = set(item1).intersection(set(item2))
        for item in intersect:
            priority_sum += ord(item) - 96 if ord(item) > 96 else ord(item) - 38
    return priority_sum


def part2():
    priority_sum = 0
    for x, y, z in zip(lines[::3], lines[1::3], lines[2::3]):
        intersect = set(x).intersection(set(y))
        intersect = intersect.intersection(set(z))
        for item in intersect:
            priority_sum += ord(item) - 96 if ord(item) > 96 else ord(item) - 38
    return priority_sum


if __name__ == '__main__':
    print(f"Part 1: {(p1:=part1())}")
    #submit(p1)
    print(f"Part 2: {(p2:=part2())}")
    submit(p2)