from aocd import data, submit
import numpy as np
"""
Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1
Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6
Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8
"""
#16 20 30 34

#16 * 5 + 20 * -1 + 30 * 0 + 34 * -1 =  26
#16 *-1 + 20 *  3 + 30 *-1 + 34 * 0  =  14
#16 * 0 + 20 *  0 + 30 * 4 + 34 * 0  =  120
#16 * 0 + 20 *  0 + 30 * 0 + 34 * 2  =  68 


#80		-20		0		-34
#-16	60		-30		0
#0		0		120		0
#0		0		0		68

#16 * 0 + 20 *  0 + 30 * 4 + 34 * 0  =  120
#16 * 0 + 20 *  0 + 30 * 0 + 34 * 2  =  68 
# 2970240

def part1():
	all = [[int(ingredient.replace(',','')) for ingredient in line.split(' ')[2::2]] for line in data.splitlines()]
	t_all = np.transpose(all)
	best = 0
	for i in range(101):
		for j in range(101):
			for k in range(101):
				if i+j+k > 100:
					break
				l = 100 - i - j- k
				best = max(best,score1(t_all,[i,j,k,l]))
	return best

def score1(all,qt):
	total_score = 1
	matrix = []
	for i in all[0:-1]:
		matrix.append(i * qt)
	for m in matrix:
		total_score = total_score * sum(m) if sum(m) > 0 else 0
	return total_score


def part2():
	all = [[int(ingredient.replace(',','')) for ingredient in line.split(' ')[2::2]] for line in data.splitlines()]
	t_all = np.transpose(all)
	best = 0
	for i in range(101):
		for j in range(101):
			for k in range(101):
				if i+j+k > 100:
					break
				l = 100 - i - j- k
				best = max(best,score2(t_all,[i,j,k,l]))
	return best

def score2(all,qt):
	total_score = 1
	matrix = []
	for i in all[0:-1]:
		matrix.append(i * qt)
	if sum(all[-1] * qt) != 500:
		return 0
	for m in matrix:
		total_score = total_score * sum(m) if sum(m) > 0 else 0
	return total_score


if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	submit(part2())