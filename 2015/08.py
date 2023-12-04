from aocd import data, submit

def part1():
	sum = 0
	for i, line in enumerate(data.splitlines()):
		# if i > 20:
		# 	break
		sum = sum + len(line) - len(bytes(line[1:-1], "utf-8").decode("unicode_escape"))
		#print(len(line),len(bytes(line, "utf-8").decode("unicode_escape"))-2)
	return sum

def part2():
	sum = 0
	for i, line in enumerate(data.splitlines()):
		sum = sum + len(str(str(line.encode()).replace('"','\\"'))) - 1 - len(line)
		# print(line			,str(str(line.encode()).replace('"','\\"'))) 
		# print(len(line)		,len(str(str(line.encode()).replace('"','\\"'))))
		#print("\n")
	return sum


if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	submit(part2())