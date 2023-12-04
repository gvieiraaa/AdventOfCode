from aocd import data, submit, lines #, numbers

def part1():
	numbers = [int(x) for x in data.split(',')]
	fishes = dict((x,numbers.count(x)) for x in set(numbers))
	for i in range(6,9):
		fishes[i] = 0
	fishes[0] = 0
	for _ in range(80):
		new = 	{0:fishes[1]
				,1:fishes[2]
				,2:fishes[3]
				,3:fishes[4]
				,4:fishes[5]
				,5:fishes[6]
				,6:fishes[7] + fishes[0]
				,7:fishes[8]
				,8:fishes[0]}
		fishes = new

	return sum([x for x in fishes.values()])

def part2():
	numbers = [int(x) for x in data.split(',')]
	fishes = dict((x,numbers.count(x)) for x in set(numbers))
	for i in range(6,9):
		fishes[i] = 0
	fishes[0] = 0
	for _ in range(256):
		new = 	{0:fishes[1]
				,1:fishes[2]
				,2:fishes[3]
				,3:fishes[4]
				,4:fishes[5]
				,5:fishes[6]
				,6:fishes[7] + fishes[0]
				,7:fishes[8]
				,8:fishes[0]}
		fishes = new

	return sum([x for x in fishes.values()])


if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	submit(part2())