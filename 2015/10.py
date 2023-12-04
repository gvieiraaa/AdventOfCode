from aocd import data, submit
from itertools import groupby

def lookandsay(num):
	return "".join(str(len(list(num))) + quantity for quantity, num in groupby(num))


def part1():
	string = lookandsay(data)
	for _ in range(40 - 1):
		string = lookandsay(string)
	return len(string)

def part2():
	string = lookandsay(data)
	for _ in range(50 - 1):
		string = lookandsay(string)
	return len(string)


if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	submit(part2())