from aocd import data, submit
import re

# IncrementalLetters(count,string := "") {
#   string .= (count<26?"":A_ThisFunc.(count//26-1,string)) Chr(Mod(count,26)+97)
#   return string
# }

def increment(string):
	if not len(string):
		return "a"
	elif string[-1:] != "z":
		return string[0:-1] + chr(ord(string[-1:]) + 1)
	else:
		return increment(string[0:-1]) + "a"

def check_abc(string):
	for i in range(ord("a"),ord("z") - 1):
		check = chr(i) + chr(i+1) + chr(i+2)
		if string.count(check):
			return True
	return False


def part1():
	current_data = data
	re_double = re.compile(r"(.)\1")
	re_letters = re.compile(r"[iol]")
	while True:
		if re_letters.search(current_data) or not check_abc(current_data) or len(re_double.findall(current_data)) < 2:
			current_data = increment(current_data)
			continue
		else:
			return current_data
		

def part2():
	current_data = increment(part1())
	re_double = re.compile(r"(.)\1")
	re_letters = re.compile(r"[iol]")
	while True:
		if re_letters.search(current_data) or not check_abc(current_data) or len(re_double.findall(current_data)) < 2:
			current_data = increment(current_data)
			continue
		else:
			return current_data


if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	submit(part2())