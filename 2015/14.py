from aocd import data, submit
import re
import math
"""
Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.
Cupid can fly 8 km/s for 17 seconds, but then must rest for 114 seconds.
Prancer can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Donner can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 11 km/s for 12 seconds, but then must rest for 125 seconds.
Comet can fly 21 km/s for 6 seconds, but then must rest for 121 seconds.
Blitzen can fly 18 km/s for 3 seconds, but then must rest for 50 seconds.
Vixen can fly 20 km/s for 4 seconds, but then must rest for 75 seconds.
Dancer can fly 7 km/s for 20 seconds, but then must rest for 119 seconds.
"""

def part1():
	rein = [(int((lines.split(' ')[3])),int(lines.split(' ')[6]),int(lines.split(' ')[13])) for lines in data.splitlines()]
	target = 2503
	fastest = 0
	for r in rein:
		full_cicles = (target // (r[1] + r[2])) * r[0] * r[1]
		partial = r[0] * r[1] if (target % (r[1] + r[2])) > r[1] else r[0] * (target % (r[1] + r[2]))
		fastest = max(fastest,full_cicles + partial)
	return fastest

def part2():
	target = 2503
	rein = [(int((lines.split(' ')[3])),int(lines.split(' ')[6]),int(lines.split(' ')[13])) for lines in data.splitlines()]
	score = [0 for _ in rein]
	for i in range(2503):
		fastest = 0
		all = []
		for r in rein:
			full_cicles = (i // (r[1] + r[2])) * r[0] * r[1]
			partial = r[0] * r[1] if (i % (r[1] + r[2])) > r[1] else r[0] * (i % (r[1] + r[2]))
			all.append(full_cicles + partial)
			fastest = max(fastest,full_cicles + partial)
		for n, each in enumerate(all):
			if each == fastest:
				score[n] = score[n] + 1
	return max(score) - 1

if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	#submit(part2())