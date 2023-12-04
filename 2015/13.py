from aocd import data, submit
from itertools import permutations, combinations

def part1():
	signal = {"gain":+1,"lose":-1}
	names = [line.split(" ")[0] for line in data.splitlines()[0::7]]
	scores = {(line.split(" ")[0],line.split(" ")[-1][0:-1]):signal[line.split(" ")[2]] * int(line.split(" ")[3]) for line in data.splitlines()}
	p = permutations(names)
	highest = 0
	for permute in p:
		sum = 0
		for i, person in enumerate(permute):
			index1 = (i-1) % len(permute)
			index2 = (i+1) % len(permute)
			sum = sum + scores[(person,permute[index1])] + scores[(person,permute[index2])]
		highest = max(highest,sum)
	return highest

def part2():
	signal = {"gain":+1,"lose":-1}
	names = [line.split(" ")[0] for line in data.splitlines()[0::7]]
	scores = {(line.split(" ")[0],line.split(" ")[-1][0:-1]):signal[line.split(" ")[2]] * int(line.split(" ")[3]) for line in data.splitlines()}
	for name in names:
		scores[('Me',name)] = 0
		scores[(name,'Me')] = 0
	names.append('Me')
	p = permutations(names)
	highest = 0
	for permute in p:
		sum = 0
		for i, person in enumerate(permute):
			index1 = (i-1) % len(permute)
			index2 = (i+1) % len(permute)
			sum = sum + scores[(person,permute[index1])] + scores[(person,permute[index2])]
		highest = max(highest,sum)
	return highest



# def part2():
# 	signal = {"gain":+1,"lose":-1}
# 	names = [line.split(" ")[0] for line in data.splitlines()[0::7]]
# 	scores = {(line.split(" ")[0],line.split(" ")[-1][0:-1]):signal[line.split(" ")[2]] * int(line.split(" ")[3]) for line in data.splitlines()}
# 	p = permutations(names)
# 	highest = 0
# 	for permute in p:
# 		most_hated = 999
# 		sum = 0
# 		for i, person in enumerate(permute):
# 			index1 = (i-1) % len(permute)
# 			index2 = (i+1) % len(permute)
# 			most_hated = min(most_hated,scores[(person,permute[index1])] + scores[(permute[index1],person)])
# 			sum = sum + scores[(person,permute[index1])] + scores[(person,permute[index2])]
# 		highest = max(highest,sum + most_hated)
# 	return highest
	


if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	#submit(part2())