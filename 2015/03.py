from aocd import data, submit

x = 0
y = 0
houses = {}
houses[(0,0)] = 1
counter = 1

for next in data[0:]:
	match next:
		case "<":
			x = x - 1
		case ">":
			x = x + 1
		case "^":
			y = y - 1
		case "v":
			y = y + 1
	houses[(x,y)] = houses.get((x,y),0) + 1

# submit(len(houses))

# PART 2

x = 0
y = 0
houses = {}
houses[(0,0)] = 2

for next in data[0::2]:
	match next:
		case "<":
			x = x - 1
		case ">":
			x = x + 1
		case "^":
			y = y - 1
		case "v":
			y = y + 1
	houses[(x,y)] = houses.get((x,y),0) + 1

x = 0
y = 0
for next in data[1::2]:
	match next:
		case "<":
			x = x - 1
		case ">":
			x = x + 1
		case "^":
			y = y - 1
		case "v":
			y = y + 1
	houses[(x,y)] = houses.get((x,y),0) + 1

submit(len(houses))