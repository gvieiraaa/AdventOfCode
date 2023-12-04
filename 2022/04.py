from aocd import data, submit, lines #, numbers

def part1():
    counter = 0
    for line in lines:
        x, y = line.split(',')
        x1, x2 = map(int, x.split('-'))
        y1, y2 = map(int, y.split('-'))
        x_list = list(range(x1, x2 + 1))
        y_list = list(range(y1, y2 + 1))
        if all(x in y_list for x in x_list) or all(y in x_list for y in y_list):
            counter += 1
    return counter

def part2():
    counter = 0
    for line in lines:
        x, y = line.split(',')
        x1, x2 = map(int, x.split('-'))
        y1, y2 = map(int, y.split('-'))
        x_list = list(range(x1, x2 + 1))
        y_list = list(range(y1, y2 + 1))
        if any(x in y_list for x in x_list) or any(y in x_list for y in y_list):
            counter += 1
    return counter


if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    submit(part1())
    print(f"Part 2: {part2()}")
    submit(part2())