from aocd import data, submit
import re




def part1():
	counter = 0
	exclude_re = re.compile(r"(ab|cd|pq|xy)")
	vowels_re = re.compile(r"[aeiou]")
	repeat_re = re.compile(r"(.)\1")
	for line in data.splitlines():
		if exclude_re.search(line):
			continue
		if len(vowels_re.findall(line)) < 3:
			continue
		if repeat_re.search(line):
			counter = counter + 1
	print(counter)


def part2():
	counter = 0
	twice_re = re.compile(r"(..).*\1")
	rep_re = re.compile(r"(.).\1")
	for line in data.splitlines():
		if not twice_re.search(line):
			continue
		if not rep_re.search(line):
			continue
		counter = counter + 1
	submit(counter)



if __name__ == '__main__':
	#part1()
	part2()