from aocd import data, submit, lines #, numbers

def part1():
	pos = [0, 0]
	for line in lines:
		match line.split(' '):
			case ['forward', n]:
				pos[0] += int(n)
			case ['down', n]:
				pos[1] += int(n)
			case ['up', n]:
				pos[1] -= int(n)
	return pos[0] * pos[1]

def part2():
	aim = 0
	pos = [0, 0]
	for line in lines:
		match line.split(' '):
			case ['forward', n]:
				pos[0] += int(n)
				pos[1] += int(n) * aim
			case ['down', n]:
				aim += int(n)
			case ['up', n]:
				aim -= int(n)
	return pos[0] * pos[1]


if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	submit(part2())