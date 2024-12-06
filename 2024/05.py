from aocd import data, submit
import math, re, itertools, functools, collections, string, dataclasses

data2 = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

lines = data.splitlines()

def part1() -> int:
    orders, pages = data.split("\n\n")
    total = 0
    for page in pages.splitlines():
        valid = True
        dict_page = [int(x) for x in page.split(",")]
        for order in orders.splitlines():
            o1, o2 = (int(x) for x in order.split("|"))
            if o1 not in dict_page or o2 not in dict_page:
                continue
            io1 = dict_page.index(o1)
            io2 = dict_page.index(o2)
            if io1 > io2:
                valid = False
        if valid:
            total += dict_page[len(dict_page)//2]

    return total

def part2() -> int:
    orders, pages = data.split("\n\n")
    total = 0
    for page in pages.splitlines():
        valid = True
        dict_page = [int(x) for x in page.split(",")]
        relevant_orders = []
        for order in orders.splitlines():
            o1, o2 = (int(x) for x in order.split("|"))
            if o1 not in dict_page or o2 not in dict_page:
                continue
            io1 = dict_page.index(o1)
            io2 = dict_page.index(o2)
            relevant_orders.append([o1, o2])
            if io1 > io2:
                valid = False
        if not valid:
            prec = {x: set() for x in dict_page}
            for x, y in relevant_orders:
                prec[x].add(y)
            end = sorted(dict_page, key=lambda x: len(prec[x]))
            total += end[len(end)//2]
    return total


if __name__ == "__main__":
    print(f"Part 1: {(p1:=part1())}")
    submit(p1, part="a")
    print(f"Part 2: {(p2:=part2())}")
    submit(p2, part="b")