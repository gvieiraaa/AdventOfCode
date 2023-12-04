from aocd import data, submit

def part1():
	position = [1,1]
	code = ''
	for line in data.splitlines():
		for letter in line:
			match letter:
				case 'L':
					position[1] = max(0,position[1] - 1)
				case 'R':
					position[1] = min(2,position[1] + 1)
				case 'U':
					position[0] = max(0,position[0] - 1)
				case 'D':
					position[0] = min(2,position[0] + 1)
		code += str(position[0] * 3 + position[1] + 1)
	return code


def part2():
	lock = [[False,False,'1',False,False],[False,'2','3','4',False],['5','6','7','8','9'],[False,'A','B','C',False],[False,False,'D',False,False]]
	position = [2,1]
	code = ''
	for line in data.splitlines():
		for letter in line:
			match letter:
				case 'L':
					position[1] = position[1] - 1 if position[1] - 1 >= 0 and lock[position[0]][position[1] - 1] else position[1]
				case 'R':
					position[1] = position[1] + 1 if position[1] + 1 <= 4 and lock[position[0]][position[1] + 1] else position[1]
				case 'U':
					position[0] = position[0] - 1 if position[0] - 1 >= 0 and lock[position[0] - 1][position[1]] else position[0]
				case 'D':
					position[0] = position[0] + 1 if position[0] + 1 <= 4 and  lock[position[0] + 1][position[1]] else position[0]
		code += lock[position[0]][position[1]]
	return code


if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	submit(part2())