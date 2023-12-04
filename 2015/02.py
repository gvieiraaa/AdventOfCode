from aocd import data, submit
import math

sum = 0
for line in data.split("\n"):
	sides = [int(x) for x in line.split("x")]
	sum = sum + 2 * (sides[0] * sides[1] + sides[0] * sides[2] + sides[1] * sides[2]) + min(sides[0] * sides[1],sides[0] * sides[2],sides[1] * sides[2])

print(sum)
#submit(sum)

#part 2

sum = 0
for line in data.split("\n"):
	sides = sorted([int(x) for x in line.split("x")])
	sum = sum + 2*(sides[0] + sides[1]) + math.prod(sides)
print(sum)
#submit(sum)