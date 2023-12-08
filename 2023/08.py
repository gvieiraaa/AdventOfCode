from aocd import data, submit
import math, re, itertools, functools, collections, string, dataclasses

lines = data.splitlines()

def part1() -> int:
    lines = data.splitlines()
    instructions = lines[0]
    nodes = lines[2:]
    all_nodes = {}
    for node in nodes:
        source, *destinations = node.replace("= (", "").replace(",","").replace(")", "").split()
        all_nodes[source] = destinations
    current = "AAA"
    end = "ZZZ"
    for i, cycle in enumerate(itertools.cycle(instructions), start=1):
        current = all_nodes[current][0 if cycle == "L" else 1]
        if current == end:
            return i

def part2() -> int:
    lines = data.splitlines()
    instructions = lines[0]
    nodes = lines[2:]
    all_nodes = {}
    for node in nodes:
        source, *destinations = node.replace("= (", "").replace(",","").replace(")", "").split()
        all_nodes[source] = destinations
    results = []
    current_nodes = [node for node in all_nodes.keys() if node.endswith("A")]
    for curr in current_nodes:
        for i, cycle in enumerate(itertools.cycle(instructions), start=1):
            curr = all_nodes[curr][0 if cycle == "L" else 1]
            if curr.endswith("Z"):
                results.append(i)
                break
    return math.lcm(*results)


if __name__ == "__main__":
    print(f"Part 1: {(p1:=part1())}")
    submit(p1, part="a")
    print(f"Part 2: {(p2:=part2())}")
    submit(p2, part="b")