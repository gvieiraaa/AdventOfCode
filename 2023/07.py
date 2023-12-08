from aocd import data, submit
import math, re, itertools, functools, collections, string, dataclasses

def tr1(data: str) -> str:
    tr = str.maketrans({
        "A": "A", "K": "B", "Q": "C", "J": "D", "T": "E", "9": "F", "8": "G", "7": "H", "6": "I", "5": "J", "4": "K", "3": "L", "2": "M",
    })
    return data.translate(tr)

def get_type1(hand: str) -> int:
    uniques_set = set(hand)
    count = sorted([hand.count(n) for n in uniques_set], reverse=True)
    match count:
        case [5]: return 1
        case [4, 1]: return 2
        case [3, 2]: return 3
        case [3, 1, 1]: return 4
        case [2, 2, 1]: return 5
        case [2, *_]: return 6
        case _: return 7

def tr2(data: str) -> str:
    tr = str.maketrans({
        "A": "A", "K": "B", "Q": "C", "J": "Z", "T": "E", "9": "F", "8": "G", "7": "H", "6": "I", "5": "J", "4": "K", "3": "L", "2": "M",
    })
    return data.translate(tr)

def get_type2(hand: str) -> int:
    jokers = hand.count("J")
    if jokers == 5:
        return 1
    uniques_set = set(hand.replace("J", ""))
    count = sorted([hand.count(n) for n in uniques_set], reverse=True)
    count[0] += jokers
    match count:
        case [5]: return 1
        case [4, 1]: return 2
        case [3, 2]: return 3
        case [3, 1, 1]: return 4
        case [2, 2, 1]: return 5
        case [2, *_]: return 6
        case _: return 7

def part1() -> int:
    hands = [line.split() for line in data.splitlines()]
    winnings = 0
    all_hands = []
    for hand in hands:
        all_hands.append((get_type1(hand[0]), tr1(hand[0]), hand[1]))
    all_hands.sort(reverse=True)
    for i, (_, _, bid) in enumerate(all_hands, start=1):
        winnings += i * int(bid)

    return winnings

def part2() -> int:
    hands = [line.split() for line in data.splitlines()]
    winnings = 0
    all_hands = []
    for hand in hands:
        all_hands.append((get_type2(hand[0]), tr2(hand[0]), hand[1]))
    all_hands.sort(reverse=True)
    for i, (_, _, bid) in enumerate(all_hands, start=1):
        winnings += i * int(bid)
    return winnings


if __name__ == "__main__":
    print(f"Part 1: {(p1:=part1())}")
    submit(p1, part="a")
    print(f"Part 2: {(p2:=part2())}")
    submit(p2, part="b")

