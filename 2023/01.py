from aocd import data, submit


def part1(data: str):
    sum_all = 0
    for d in data.splitlines():
        nums = list(filter(str.isdecimal, d))
        sum_all += int(nums[0] + nums[-1])
    return sum_all

def part2(data: str):
    sum_all = 0
    numbers_str = "one two three four five six seven eight nine".split()
    for d in data.splitlines():
        for i, number in enumerate(numbers_str, start=1):
            d = d.replace(number, number + str(i) + number)
        nums = list(filter(str.isdecimal, d))
        sum_all += int(nums[0] + nums[-1])
    return sum_all


if __name__ == "__main__":
    print(f"Part 1: {(p1:=part1(data))}")
    submit(p1, part="a")
    print(f"Part 2: {(p2:=part2(data))}")
    submit(p2, part="b")