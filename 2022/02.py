from aocd import data, submit, lines #, numbers

def part1():
    score_fixed = {'X': 1, 'Y': 2, 'Z': 3}
    winnings = {'A':{'X':3, 'Y':6, 'Z':0},
        'B':{'X':0, 'Y':3, 'Z': 6},
        'C':{'X':6, 'Y':0, 'Z': 3}}
    score = 0
    for match in lines:
        elf, me = match.split(' ')
        score += score_fixed[me]
        score += winnings[elf][me]
    return score

def part2():
    winnings = {'A':{'X':0+3, 'Y':3+1, 'Z':6+2},
                'B':{'X':0+1, 'Y':3+2, 'Z':6+3},
                'C':{'X':0+2, 'Y':3+3, 'Z': 6+1}}
    score = 0
    for match in lines:
        elf, me = match.split(' ')
        score += winnings[elf][me]
    return score


if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    #submit(part1())
    print(f"Part 2: {part2()}")
    submit(part2())