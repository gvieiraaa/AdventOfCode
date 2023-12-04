from aocd import data, submit
import numpy as np

def part1():
	valid = 0
	for line in data.splitlines():
		s = sorted([int(x) for x in line.split()])
		if s[0] + s[1] > s[2]:
			valid += 1
	return valid

def part2():
	n = [[int(x) for x in line.split()] for line in data.splitlines()]
	new = []
	for i in range(len(n) // 3):
		for j in range(3):
			new.append([n[i*3][j],n[i*3+1][j],n[i*3+2][j]])
	#print(n)
	#print('\n\n')

	#print(new)
	valid = 0
	for line in new:
		s = sorted(line)
		if s[0] + s[1] > s[2]:
			valid += 1
	return valid


if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	#submit(part2())