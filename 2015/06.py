from aocd import data, submit
import re




def part1():
	lights = [[False for _ in range(1000)] for _ in range(1000)]
	for line in data.splitlines():
		match line.split(" "):
			case ["toggle",x,_,y]:
				coord1 = [int(f) for f in x.split(",")]
				coord2 = [int(f) for f in y.split(",")]
				for i in range(coord1[0],coord2[0]+1):
					for j in range(coord1[1],coord2[1]+1):
						lights[i][j] = not lights[i][j]
			case ["turn","on",x,_,y]:
				coord1 = [int(f) for f in x.split(",")]
				coord2 = [int(f) for f in y.split(",")]
				for i in range(coord1[0],coord2[0]+1):
					for j in range(coord1[1],coord2[1]+1):
						lights[i][j] = True
			case ["turn","off",x,_,y]:
				coord1 = [int(f) for f in x.split(",")]
				coord2 = [int(f) for f in y.split(",")]
				for i in range(coord1[0],coord2[0]+1):
					for j in range(coord1[1],coord2[1]+1):
						lights[i][j] = False
	sum = 0
	for x in lights:
		sum = sum + x.count(True)

	print(sum)

def part2():
	lights = [[0 for _ in range(1000)] for _ in range(1000)]
	for line in data.splitlines():
		match line.split(" "):
			case ["toggle",x,_,y]:
				coord1 = [int(f) for f in x.split(",")]
				coord2 = [int(f) for f in y.split(",")]
				for i in range(coord1[0],coord2[0]+1):
					for j in range(coord1[1],coord2[1]+1):
						lights[i][j] = lights[i][j] + 2
			case ["turn","on",x,_,y]:
				coord1 = [int(f) for f in x.split(",")]
				coord2 = [int(f) for f in y.split(",")]
				for i in range(coord1[0],coord2[0]+1):
					for j in range(coord1[1],coord2[1]+1):
						lights[i][j] = lights[i][j] + 1
			case ["turn","off",x,_,y]:
				coord1 = [int(f) for f in x.split(",")]
				coord2 = [int(f) for f in y.split(",")]
				for i in range(coord1[0],coord2[0]+1):
					for j in range(coord1[1],coord2[1]+1):
						lights[i][j] = max(0,lights[i][j] - 1)
	all = 0
	for k in lights:
		all = sum(k) + all

	print(all)


if __name__ == '__main__':
	#part1()
	part2()