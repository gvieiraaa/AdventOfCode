from aocd import data, submit, lines #, numbers

def part1():
	elves_calories = data.split('\n\n')
	return max([sum(map(int, elve.split('\n'))) for elve in elves_calories])

def part2():
	elves_calories = data.split('\n\n')
	elves_sum = [sum(map(int, elve.split('\n'))) for elve in elves_calories]
	elves_sum = sorted(elves_sum)
	return sum(elves_sum[-3:])


if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	submit(part2())