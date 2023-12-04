from aocd import data, submit

def part1():
	instructions = data.splitlines()
	register = {'a':0,'b':0}
	signal = {'+':1,'-':-1}
	pointer = 0
	while (0 <= pointer < len(instructions)):
		match instructions[pointer].replace(',','').split():
			case ['hlf',r]:
				register[r] /= 2
				pointer += 1
			case ['tpl',r]:
				register[r] *= 3
				pointer += 1
			case ['inc',r]:
				register[r] += 1
				pointer += 1
			case ['jmp',s]:
				pointer += signal[s[0]] * int(s[1:])
			case ['jie',r,s]:
				pointer += signal[s[0]] * int(s[1:]) if register[r] % 2 == 0 else 1
			case ['jio',r,s]:
				pointer += signal[s[0]] * int(s[1:]) if register[r] == 1 else 1
	return register['b']


def part2():
	instructions = data.splitlines()
	register = {'a':1,'b':0}
	signal = {'+':1,'-':-1}
	pointer = 0
	while (0 <= pointer < len(instructions)):
		match instructions[pointer].replace(',','').split():
			case ['hlf',r]:
				register[r] /= 2
				pointer += 1
			case ['tpl',r]:
				register[r] *= 3
				pointer += 1
			case ['inc',r]:
				register[r] += 1
				pointer += 1
			case ['jmp',s]:
				pointer += signal[s[0]] * int(s[1:])
			case ['jie',r,s]:
				pointer += signal[s[0]] * int(s[1:]) if register[r] % 2 == 0 else 1
			case ['jio',r,s]:
				pointer += signal[s[0]] * int(s[1:]) if register[r] == 1 else 1
	return register['b']


if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	submit(part2())