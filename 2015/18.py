from aocd import data, submit

def part1():
	input = [[1 if i=='#' else 0 for i in line] for line in data.splitlines()]
	for i in range(100):
		input = gol(input)
	return sum([sum(k) for k in input])

def part2():
	input = [[1 if i=='#' else 0 for i in line] for line in data.splitlines()]
	input[0][0] = 1
	input[0][99] = 1
	input[99][0] = 1
	input[99][99] = 1
	for i in range(100):
		input = gol(input)
		input[0][0] = 1
		input[0][99] = 1
		input[99][0] = 1
		input[99][99] = 1
	return sum([sum(k) for k in input])

def gol(input):
	new = [[0 for _ in range(100)] for _ in range(100)]
	for ki in range(100):
		for kj in range(100):
			summed = sum([0 if (i<0 or i>=100 or j<0 or j>=100) else input[i][j] for i in range(ki-1,ki+2) for j in range(kj-1,kj+2)])
			if input[ki][kj] == 1 and 3 <= summed and summed <= 4:
				new[ki][kj] = 1
			elif input[ki][kj] == 0 and summed == 3:
				new[ki][kj] = 1
	return new


if __name__ == '__main__':
	#print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	submit(part2())