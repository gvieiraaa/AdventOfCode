from aocd import data, submit
import re
def part1():
	re_all = re.compile(r'(.*?)(\d+)\[(.*)\]')
	for line in data.splitlines():
		found = re_all.match(line)
		ordered = found[1].split('-')


def part2():
	return -1


if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	#print(f"Part 2: {part2()}")
	#submit(part2())