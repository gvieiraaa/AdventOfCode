from aocd import data, submit, lines #, numbers
from collections import Counter 

def part1():
	counter = 0
	for line in lines:
		s_digits = line.split(' | ')[1]
		digits = s_digits.split(' ')

		for digit in digits:
			l = len(digit)
			if l == 2 or l == 3 or l == 4 or l == 7:
				counter += 1
	return counter

def part2():
	nums = {'012456': '0', '25': '1', '02346': '2', '02356': '3', '1235': '4', \
			'01356': '5', '013456': '6', '025': '7', '0123456': '8', '012356': '9'}
	tot = 0

	for r in [d.split(' | ') for d in lines]:
		z, a = r[0].split(' '), r[1].split(' ')
		t = ''.join(z)

		m = [''] * 7
		d = Counter(''.join(t))
		dr = {}
		for k, v in d.items():
			dr.setdefault(v, [])
			dr[v].append(k)

		m[1], m[4], m[5] = dr[6][0], dr[4][0], dr[9][0]
		m[2] = [x for x in z if len(x) == 2][0].replace(m[5], '')
		m[0] = list(set([x for x in z if len(x) == 3][0]) - set(m[2] + m[5]))[0]
		m[3] = list(set([x for x in z if len(x) == 4][0]) - set(m[1] + m[2]+m[5]))[0]
		m[6] = list(set([x for x in z if len(x) == 7][0]) - set(m[:-1]))[0]

		a2 = [''.join(sorted([str(m.index(j)) for j in i])) for i in a]
		tot += int(''.join([*map(nums.get, a2)]))

	return tot


if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	submit(part2())