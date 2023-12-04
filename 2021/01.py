from aocd import data, submit, lines, numbers

def part1():
	total = 0
	for n in range(len(numbers)-1):
		if numbers[n] < numbers[n+1]:
			total += 1
	return total

def part2():
	total = 0
	new = [sum(numbers[n:n+3]) for n in range(len(numbers)-1)]
	for n in range(len(new)-1):
		if new[n] < new[n+1]:
			total += 1
	return total


if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	submit(part2())