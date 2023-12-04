from aocd import data, submit

def part1():
	position = [0,0]
	direction = [(1,0),(0,-1),(-1,0),(0,1)]
	pointer = 0
	for instruction in data.split(', '):
		pointer += 1 if instruction[0:1] == 'R' else -1
		position = [(i+j * int(instruction[1:])) for i,j in zip(position,direction[pointer % 4])]
	return sum([abs(x) for x in position])


def part2():
	position = [0,0]
	direction = [(1,0),(0,-1),(-1,0),(0,1)]
	pointer = 0
	history = [(0,0)]
	for instruction in data.split(', '):
		pointer += 1 if instruction[0:1] == 'R' else -1
		for _ in range(int(instruction[1:])):
			position = [(i+j * 1) for i,j in zip(position,direction[pointer % 4])]
			tp = (position[0],position[1])
			print(tp)
			if tp in history:
				return sum([abs(x) for x in position])
			else:
				history.append(tp)
		


if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	#submit(part2())