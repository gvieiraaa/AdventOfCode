from aocd import data, submit
import math, re, itertools, functools, collections, string

lines = data.splitlines()

def part1() -> int:
    sum_ = 0
    for line in lines:
        _, winning_str, chosen_str = line.replace(":", "|").split("|")
        winning_nums = set(map(int, winning_str.split()))
        chosen_nums = set(map(int, chosen_str.split()))
        winning = winning_nums & chosen_nums
        if winning:
            sum_ += 2 ** (len(winning) - 1)
    return sum_

def part2() -> int:
    additional_cards = [0 for _ in range(len(lines))]
    for i, line in enumerate(lines):
        _, winning_str, chosen_str = line.replace(":", "|").split("|")
        winning_nums = set(map(int, winning_str.split()))
        chosen_nums = set(map(int, chosen_str.split()))
        winning = winning_nums & chosen_nums
        if winning:
            copies = additional_cards[i]
            for n in range(i, i + len(winning)):
                additional_cards[n + 1] += 1 + copies
    return sum(additional_cards) + len(lines)



if __name__ == "__main__":
    print(f"Part 1: {(p1:=part1())}")
    submit(p1, part="a")
    print(f"Part 2: {(p2:=part2())}")
    submit(p2, part="b")