from aocd import data, submit
import itertools

def part1():
	sum_all = 0
	d = [int(v) for v in data.splitlines()]
	for i in range(len(d)):
		for n in itertools.combinations(d,i+1):
			if sum(n) == 150:
				sum_all = sum_all + 1
	return sum_all


def part2():
	min_containers = 99999
	sum_all = 0
	d = [int(v) for v in data.splitlines()]
	for i in range(len(d)):
		for n in itertools.combinations(d,i+1):
			if sum(n) == 150:
				min_containers = min(min_containers,len(n))
	for i in range(len(d)):
		for n in itertools.combinations(d,i+1):
			if sum(n) == 150 and len(n) == min_containers:
				sum_all = sum_all + 1
	return sum_all

if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	submit(part2())