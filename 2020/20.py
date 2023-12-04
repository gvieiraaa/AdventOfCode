from aocd import data, submit
import numpy as np

def part1():
	tiles = data.split('\n\n')
	instances = []
	for t in tiles:
		instances.append(tile(t))
	corners = []
	each = [i.get_all_sides() for i in instances]
	all = []
	product = 1
	for i in each:
		for j in i:
			all.append(j)
	for indexi, i in enumerate(each):
		sum_ = 0
		for j in i:
			sum_ += all.count(j)
		if sum_ == 12:
			product *= instances[indexi].num
	return product

def part2():
	return -1

class tile:
	def __init__(self,raw):
		self.raw = raw
		lines = raw.splitlines()
		self.num = int(lines[0].split()[1].replace(':',''))
		self.data = np.array([[1 if j=='#' else 0 for j in k] for k in lines[1:]])
	
	def rotate(self):
		self.data = np.rot90(self.data)
		return self.data

	def flip(self,orientation):
		self.data = np.flip(self.data,orientation)

	def get_all_sides(self):
		side_list = []
		a = self.data[0]
		b = self.data[-1]
		side_list.append(''.join([str(n) for n in a]))
		side_list.append(''.join([str(n) for n in b]))
		side_list.append(''.join([str(n) for n in a[::-1]]))
		side_list.append(''.join([str(n) for n in b[::-1]]))
		self.rotate()
		a = self.data[0]
		b = self.data[-1]
		side_list.append(''.join([str(n) for n in a]))
		side_list.append(''.join([str(n) for n in b]))
		side_list.append(''.join([str(n) for n in a[::-1]]))
		side_list.append(''.join([str(n) for n in b[::-1]]))
		return side_list

if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	#submit(part2())