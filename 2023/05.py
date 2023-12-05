from aocd import data, submit
import math, re, itertools, functools, collections, string, dataclasses

lines = data.splitlines()

def is_valid(seeds: tuple, n: int) -> bool:
    for x, y in itertools.batched(seeds, 2):
        if x <= n <= x + y:
            return True
    return False

Map = collections.namedtuple("Map", ["destination", "source", "range"])

def part1() -> int:
    seeds, *maps = data.split("\n\n")
    all_maps = []
    locations = []
    for each_map in maps:
        _, *map_ranges = each_map.splitlines()
        map_ranges = tuple(Map(*map(int, map_range.split())) for map_range in map_ranges)
        all_maps.append(map_ranges)
    for start in map(int, seeds.split(":")[1].split()):
        for each_map in all_maps:
            for single in each_map:
                if single.source <= start <= single.source + single.range:
                    start = start - single.source + single.destination
                    break
        locations.append(start)
    return min(locations)

def part2() -> int:
    seeds, *maps = data.split("\n\n")
    all_maps = []
    for each_map in maps:
        _, *map_ranges = each_map.splitlines()
        map_ranges = tuple(Map(*map(int, map_range.split())) for map_range in map_ranges)
        all_maps.append(map_ranges)
    seeds_tup = tuple(map(int, seeds.split(":")[1].split()))
    for i in range(int(1e10)):
        start_i = i
        for each_map in reversed(all_maps):
            for single in each_map:
                if single.destination <= i <= single.destination + single.range:
                    i = i - single.destination + single.source
                    break
        if is_valid(seeds_tup, i):
            return start_i


if __name__ == "__main__":
    print(f"Part 1: {(p1:=part1())}")
    submit(p1, part="a")
    print(f"Part 2: {(p2:=part2())}")
    submit(p2, part="b")