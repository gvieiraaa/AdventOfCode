from os import kill
from aocd import data, submit
import re
"""
Sue 1: children: 1, cars: 8, vizslas: 7
Sue 2: akitas: 10, perfumes: 10, children: 5
Sue 3: cars: 5, pomeranians: 4, vizslas: 1
Sue 4: goldfish: 5, children: 8, perfumes: 3
"""

def part1():
	sue_list = [Sue(i, line) for i, line in enumerate(data.splitlines())]
	known = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""".splitlines()
	for s in sue_list:
		for k in known:
			s.check_if_valid(k)
	
	for s in sue_list:
		if s.is_valid():
			return(s.num)

def part2():
	sue_list = [Sue(i, line) for i, line in enumerate(data.splitlines())]
	known = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""".splitlines()
	for s in sue_list:
		for k in known:
			s.check_if_valid2(k)
	
	for s in sue_list:
		if s.is_valid():
			return(s.num)

class Sue:
	def __init__(self,i, line):
		self.line = line
		self.num = i + 1
		self.info = {}
		self.valid = True
		self.valid2 = True
		self._parse()
	
	def _parse(self):
		three = self.line.split(' ')[2:]
		for i, j in zip(three[0::2],three[1::2]):
			self.info[i.replace(':','')] = int(j.replace(',',''))

	def check_if_valid(self,imported):
		current_data = imported.split(': ')
		if self.valid == False:
			return False
		self.valid = (self.info[current_data[0]] == int(current_data[1])) if current_data[0] in self.info else True
		return self.valid

	def check_if_valid2(self,imported):
		current_data = imported.split(': ')
		if self.valid == False:
			return False
		if current_data[0] in ['cats','trees']:
			self.valid = (self.info[current_data[0]] > int(current_data[1])) if current_data[0] in self.info else True
		elif current_data[0] in ['pomeranians','goldfish']:
			self.valid = (self.info[current_data[0]] < int(current_data[1])) if current_data[0] in self.info else True
		else:
			self.valid = (self.info[current_data[0]] == int(current_data[1])) if current_data[0] in self.info else True
		return self.valid

	def is_valid(self):
		return self.valid

if __name__ == '__main__':
	#print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	submit(part2())