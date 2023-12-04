from aocd import data, submit
from functools import reduce

def part1():
	count = 0
	max_gifts = int(data)
	while True:
		count += 1
		t = sum(list(map(lambda x: x * 10,factors(count))))
		if t >= max_gifts:
			return count

def part2():
	count = 0
	max_gifts = int(data)
	while True:
		count += 1
		t = sum(list(map(lambda x: x * 11 if count <= x * 50 else 0,factors(count))))
		if t >= max_gifts:
			return count

def factors(n):    
	return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

if __name__ == '__main__':
	#print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	#submit(part2())