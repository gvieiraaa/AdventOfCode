from aocd import data, submit, lines, numbers

def part1():
    for i in range(9999):
        if len(set(data[i:i+4])) == 4:
            return i+4

def part2():
    for i in range(9999):
        if len(set(data[i:i+14])) == 14:
            return i+14

if __name__ == '__main__':
    print(f"Part 1: {(p1:=part1())}")
    submit(p1)
    print(f"Part 1: {(p2:=part2())}")
    submit(p2)