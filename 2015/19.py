from aocd import data, submit
import re

def part1():
	conditions = {}
	uniques = set()
	for line in data.splitlines():
		match line.split(' '):
			case [a,"=>",b]:
				if a in conditions:
					conditions[a].append(b)
				else:
					conditions[a] = [b]
			case [a]:
				start = a
	for i, j in conditions.items():
		for k in j:
			for n in range(len(re.findall(i,start))):
				uniques.add(replace_nth(start,i,k,n+1))

	return len(uniques)

def part2():
	input = data
	molecule = input.split('\n')[-1][::-1]
	reps = {m[1][::-1]: m[0][::-1] 
			for m in re.findall(r'(\w+) => (\w+)', input)}

	count = 0
	while molecule != 'e':
		molecule = re.sub('|'.join(reps.keys()), lambda x: reps[x.group()], molecule, 1)
		count += 1
	return count


def replace_nth(string,replace,replacement,position):
	arr = string.split(replace)
	return replace.join(arr[:position]) + replacement + replace.join(arr[position:])


if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	#submit(part2())