from aocd import data, submit, lines #, numbers

def part1():
	all = data.split('\n\n')
	order = [int(n) for n in all[0].split(',')]
	boards = all[1:]
	instances = [board(single_board) for single_board in boards]
	for number in order:
		for instance in instances:
			instance.add(number)
			if instance.is_winner():
				return(instance.get_sum() * number)

	return -1

def part2():
	all = data.split('\n\n')
	order = [int(n) for n in all[0].split(',')]
	boards = all[1:]
	instances = [board(single_board) for single_board in boards]
	for number in order:
		for instance in reversed(instances):
			instance.add(number)
			if instance.is_winner():
				if len(instances) > 1:
					instances.remove(instance)
				else:
					return(instance.get_sum() * number)

class board:
	def __init__(self,raw):
		self.raw = raw
		self.array = [[int(n) for n in row.split(' ') if n] for row in self.raw.split('\n')]
		self.mark = [[False for _ in range(5)] for _ in range(5)]

	def add(self,num):
		for i in range(5):
			for j in range(5):
				if self.array[i][j] == num:
					self.mark[i][j] = True

	def is_winner(self):
		for row in self.mark:
			if all(row):
				return True
		temp = list(map(list, zip(*self.mark)))
		for row in temp:
			if all(row):
				return True
		return(False)

	def get_sum(self):
		sum = 0
		for i in range(5):
			for j in range(5):
				if self.mark[i][j] == False:
					sum += self.array[i][j]
		return(sum)

if __name__ == '__main__':
	#print(f"Part 1: {part1()}")
	#submit(part1())
	#print(f"Part 2: {part2()}")
	submit(part2())