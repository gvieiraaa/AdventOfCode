from aocd import data, submit, lines #, numbers
import numpy as np

def part1():
	coords = [[int(n) for n in line.replace(' -> ',',').split(',')] for line in lines]
	array = [[0 for _ in range(np.max(coords) + 1)] for _ in range(np.max(coords) + 1)]
	for line in coords:
		if line[0] == line[2]:
			for i in range(min(line[1],line[3]),1 + max(line[1],line[3])):
				array[line[0]][i] += 1
		if line[1] == line[3]:
			for i in range(min(line[0],line[2]),1 + max(line[0],line[2])):
				array[i][line[1]] += 1

	counter = 0
	for i in array:
		for j in i:
			if j > 1:
				counter += 1

	return(counter)

def part2():
	sign = {True:1,False:-1}
	coords = [[int(n) for n in line.replace(' -> ',',').split(',')] for line in lines]
	array = [[0 for _ in range(np.max(coords) + 1)] for _ in range(np.max(coords) + 1)]
	for line in coords:
		if line[0] == line[2]:
			for i in range(min(line[1],line[3]),1 + max(line[1],line[3])):
				array[line[0]][i] += 1
		elif line[1] == line[3]:
			for i in range(min(line[0],line[2]),1 + max(line[0],line[2])):
				array[i][line[1]] += 1
		else:
			start = [line[0],line[1]]
			end = [line[2],line[3]]
			for i in range(1 + abs(start[0] - end[0])):
				array[start[0] + i * sign[start[0] - end[0] < 0]][start[1] + i * sign[start[1] - end[1] < 0]] += 1

	counter = 0
	for i in array:
		for j in i:
			if j > 1:
				counter += 1

	return(counter)

if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	#submit(part2())