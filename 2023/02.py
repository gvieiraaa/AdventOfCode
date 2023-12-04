from aocd import data, submit #, numbers
import math

"""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

def part1(data: str) -> int:
    sum_games = 0
    for line in data.splitlines():
        limits = {"red": 12, "green": 13, "blue": 14}
        game, colors = line.split(": ")
        valid = True
        for color_set in colors.split("; "):
            for color in color_set.split(", "):
                quantity, rgb_color = color.split()
                if int(quantity) > limits[rgb_color]:
                    valid = False
        if valid:
            sum_games += int(game.split()[1])
    return sum_games

def part2(data: str) -> int:
    sum_games = 0
    for line in data.splitlines():
        max_rgb = {"red": 0, "green": 0, "blue": 0}
        _, colors = line.split(": ")
        for color_set in colors.split("; "):
            for color in color_set.split(", "):
                quantity, rgb_color = color.split()
                max_rgb[rgb_color] = max(max_rgb[rgb_color], int(quantity))
        sum_games += math.prod(max_rgb.values())
    return sum_games


if __name__ == '__main__':
    print(f"Part 1: {(p1:=part1(data))}")
    submit(p1, part="a")
    print(f"Part 2: {(p2:=part2(data))}")
    submit(p2, part="b")