from aocd import data, submit, lines #, numbers

def part1():
	crabs = [int(x) for x in data.split(',')]
	min_fuel = 999999999
	for i in range(max(crabs)):
		fuel_sum = 0
		for crab in crabs:
			fuel_sum += abs(crab - i)
		min_fuel = min(min_fuel,fuel_sum)

	return min_fuel


def part2():
	crabs = [int(x) for x in data.split(',')]
	min_fuel = 999999999
	for i in range(max(crabs)):
		fuel_sum = 0
		for crab in crabs:
			fuel_sum += term(abs(crab - i))
		min_fuel = min(min_fuel,fuel_sum)

	return int(min_fuel)

def term(n):
    return n *(n + 1) / 2

if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	submit(part2())