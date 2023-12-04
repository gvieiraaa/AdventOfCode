from aocd import data, submit
import itertools

def part1():
	lst = [int(x) for x in data.splitlines()]
	total_weight = sum(lst)
	min_entanglement = 999999999999
	for i in range(7):
		for combination in itertools.combinations(lst,i):
			if sum(combination) == total_weight / 3:
				min_entanglement = min(min_entanglement,multiply(combination))
	return min_entanglement

def part2():
	lst = [int(x) for x in data.splitlines()]
	total_weight = sum(lst)
	min_entanglement = 999999999999
	for i in range(7):
		for combination in itertools.combinations(lst,i):
			if sum(combination) == total_weight / 4:
				min_entanglement = min(min_entanglement,multiply(combination))
	return min_entanglement

def multiply(arr):
	start = 1
	for num in arr:
		start *= num
	return start

if __name__ == '__main__':
	#print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	#submit(part2())