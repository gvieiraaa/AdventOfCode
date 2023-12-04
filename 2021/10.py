from binascii import Incomplete
from sys import prefix
from aocd import data, submit, lines #, numbers
import time

pref = '([{<'
suf = ')]}>'
lot = {k: v for k, v in zip(suf,pref)}
invlot = {v: k for k, v in lot.items()}
incomplete = []

def part1():
	error_list = {k:0 for k in suf}
	for line in lines:
		parsed = []
		for char in line:
			if char in pref:
				parsed.append(char)
			elif parsed[-1] == lot[char]:
				parsed = parsed[:-1]
			else:
				#print(f'character {char} has no start.')
				error_list[char] += 1
				break
		else:
			incomplete.append(line)
			
	print(error_list)
	print(incomplete)
	return sum([value * score for value, score in zip(error_list.values(),[3,57,1197,25137])])

def part2():
	all_lines = []
	for line in incomplete:
		parsed = []
		for char in line:
			if char in suf:
				parsed = parsed[:-1]
			else:
				parsed.append(char)
		all_lines.append(parsed)
	scores = []
	pts = {'(':1,'[':2,'{':3,'<':4}
	print([''.join(line) for line in all_lines])
	for line in all_lines:
		score_sum = 0
		for char in line[::-1]:
			score_sum *= 5
			score_sum += pts[char]
			#print(f'char {char} / score sum {score_sum}')
			#time.sleep(0.3)
		scores.append(score_sum)
	scores = sorted(scores)
	return scores[len(scores)//2]

if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	submit(part2())