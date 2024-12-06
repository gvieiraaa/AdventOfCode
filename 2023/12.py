from aocd import data, submit
import math, re, itertools, functools, collections, string, dataclasses

data2 = """\
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

lines = data.splitlines()

def replace_all(s: str):
    if "?" not in s:
        return [s]
    
    with_dot = s.replace("?", ".", 1)
    with_hash = s.replace("?", "#", 1)
    
    return replace_all(with_dot) + replace_all(with_hash)
    
def total_combinations(springs, groups):
    @functools.cache
    def combinations(i, j, r):
        if j == len(groups):
            return springs.count("#", i) == 0
        if i == len(springs):
            return j == len(groups) - 1 and r == groups[j]
        n = 0
        if springs[i] != ".":
            n += combinations(i + 1, j, r + 1)
        if springs[i] != "#":
            if r == groups[j]:
                n += combinations(i + 1, j + 1, 0)
            elif r == 0:
                n += combinations(i + 1, j, 0)
        return n

    return combinations(0, 0, 0)

@functools.cache
def is_valid(s: str, damaged: tuple):
    split = re.split("\\.+", s)
    return tuple(len(x) for x in split if len(x) != 0) == damaged

def part1() -> int:
    count = 0
    for row in lines:
        springs, dmg_groups = row.split()
        dmg_groups = [int(x) for x in dmg_groups.split(",")]
        r = replace_all(springs)
        for each in r:
            if is_valid(each, dmg_groups):
                count += 1
        
    return count

def part2() -> int:
    count = 0
    for row in lines:
        springs, dmg_groups = row.split()
        springs = "?".join(itertools.repeat(springs, 5))
        dmg_groups = [int(x) for x in dmg_groups.split(",")]
        dmg_groups = dmg_groups * 5
        print(dmg_groups)
        print(springs)
        count += total_combinations(springs, dmg_groups)
        
    return count


if __name__ == "__main__":
    #print(f"Part 1: {(p1:=part1())}")
    #submit(p1, part="a")
    print(f"Part 2: {(p2:=part2())}")
    submit(p2, part="b")