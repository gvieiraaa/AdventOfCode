from aocd import data, submit, lines #, numbers

def part1():
	count = [0 for _ in range(len(lines[0][::1]))]
	for line in lines:
		for n in range(len(line)):
			count[n] = count[n] + int(line[n])
	gamma = ''.join(['1' if count[n] > len(lines)//2 else '0' for n in range(len(count))])
	epsilon = ''.join(['0' if count[n] > len(lines)//2 else '1' for n in range(len(count))])
	gamma = int(gamma,2)
	epsilon = int(epsilon,2)
	return(gamma * epsilon)


def part2():
	size = len(lines[0])
	bin_data = [int(line,2) for line in lines]
	for step in reversed(range(size)):
		count = [min(d & (1 << step),1) for d in bin_data]
		keep = 1 if sum(count) >= len(count)/2 else 0
		bin_data = [n for n in bin_data if min(n & (1 << step),1) == keep]
		if len(bin_data) == 1:
			o2 = bin_data[0]

			
	bin_data = [int(line,2) for line in lines]
	for step in reversed(range(size)):
		count = [min(d & (1 << step),1) for d in bin_data]
		keep = 0 if sum(count) >= len(count)/2 else 1
		bin_data = [n for n in bin_data if min(n & (1 << step),1) == keep]
		if len(bin_data) == 1:
			co2 = bin_data[0]

	return(o2 * co2)

if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	#submit(part2())