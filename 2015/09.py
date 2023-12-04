from aocd import data, submit
import itertools

def part1():
	distances = {(line.split(" ")[0],line.split(" ")[2]):int(line.split(" ")[4]) for line in data.splitlines()}
	locations = [x for x, _ in {x[0]:True for x, y in distances.items()}.items()]
	locations.append('Arbre')
	print(locations)
	min_sum = 99999
	for path in itertools.permutations(locations):
		sum = 0
		for i in range(len(path)-1):
			small_path = path[i:i+2]
			sum = sum + distances[small_path] if small_path in distances else sum + distances[tuple([small_path[1],small_path[0]])]
		min_sum = min(min_sum,sum)
	return min_sum


def part2():
	distances = {(line.split(" ")[0],line.split(" ")[2]):int(line.split(" ")[4]) for line in data.splitlines()}
	locations = [x for x, _ in {x[0]:True for x, y in distances.items()}.items()]
	locations.append('Arbre')
	print(locations)
	max_sum = 0
	for path in itertools.permutations(locations):
		sum = 0
		for i in range(len(path)-1):
			small_path = path[i:i+2]
			sum = sum + distances[small_path] if small_path in distances else sum + distances[tuple([small_path[1],small_path[0]])]
		max_sum = max(max_sum,sum)
	return max_sum


if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	submit(part2())