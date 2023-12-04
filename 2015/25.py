from aocd import data, submit

def part1():
	"""row 3010, column 3019."""
	total = sum(range(3010 + 3019 - 1)) + 3019
	code = 20151125
	for _ in range(total - 1):
		code = (code * 252533) % 33554393
	return code

def part2():
	return -1




if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	submit(part1())
	#print(f"Part 2: {part2()}")
	#submit(part2())