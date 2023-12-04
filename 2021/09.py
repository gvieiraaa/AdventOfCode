from aocd import data, submit, lines #, numbers
import numpy as np
import collections
from typing import Generator


def adj(x: int,y: int) -> Generator[tuple[int, int], None, None]:
	yield x + 1, y
	yield x - 1, y
	yield x, y + 1
	yield x, y - 1

def part1():

	nums = [[int(n) for n in line] for line in lines]
	size_i, size_j = len(nums), len(nums[0])
	total = 0
	for i in range(size_i):
		for j in range(size_j):
			adj = []
			for n in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
				if n[0] >= 0 and n[0] < size_i and n[1] >= 0 and n[1] < size_j:
					adj.append(nums[n[0]][n[1]])
				else:
					adj.append(9)
			if all([nums[i][j] < x for x in adj]):
				total += 1 + nums[i][j]
	return total

def part2():
	coords = collections.defaultdict(lambda: 9)
	# nums = [[int(n) for n in line] for line in lines]
	# size_i, size_j = len(nums), len(nums[0])
	# expanded = [[9 for _ in range(size_i + 2)] for _ in range(size_j + 2)]
	# for i in range(size_i):
	# 	for j in range(size_j):
	# 		expanded[i+1][j+1] = nums[i][j]
	# print(expanded)
	coords[0,0] = 1
	for x,y in adj(1,1):
		print(x,y)


if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	#submit(part2())