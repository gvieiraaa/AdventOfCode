from aocd import data, submit
import json
import re

def part1():
	re_all = re.compile(r'-?\d+')
	return sum(int(i) for i in re_all.findall(data))

def part2():
	return sum_json(json.loads(data))

def sum_json(obj):
	if isinstance(obj,int):
		return obj
	n = 0
	if isinstance(obj, dict):
		for v in obj.values():
			if v == 'red':
				return 0
			else:
				n = n + sum_json(v)
	elif isinstance(obj, list):
		for v in obj:
			n += sum_json(v)
	return n

if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	#submit(part2())