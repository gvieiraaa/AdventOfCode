from aocd import data, submit
import re

def part1():
	wires = {line.split(" -> ")[1]:line.split(" -> ")[0] for line in data.splitlines()}
	resolved = {}
	while len(wires):
		for key, value in dict(wires).items():
			match value.split(" "):
				case [x]:
					if re.match("\d+",x) or x in resolved:
						resolved[key] = int(x) if x not in resolved else resolved[x]
						wires.pop(key)
					else:
						continue
			
				case [x,"AND",y]:
					if (re.match("\d+",x) or x in resolved) and (re.match("\d+",y) or y in resolved):
						p1 = int(x) if x not in resolved else resolved[x]
						p2 = int(y) if y not in resolved else resolved[y]
						resolved[key] = p1 & p2
						wires.pop(key)
					else:
						continue

				case [x,"OR",y]:
					if (re.match("\d+",x) or x in resolved) and (re.match("\d+",y) or y in resolved):
						p1 = int(x) if x not in resolved else resolved[x]
						p2 = int(y) if y not in resolved else resolved[y]
						resolved[key] = p1 | p2
						wires.pop(key)
					else:
						continue
					
				case [x,"RSHIFT",y]:
					if (re.match("\d+",x) or x in resolved) and (re.match("\d+",y) or y in resolved):
						p1 = int(x) if x not in resolved else resolved[x]
						p2 = int(y) if y not in resolved else resolved[y]
						resolved[key] = p1 >> p2
						wires.pop(key)
					else:
						continue

				case [x,"LSHIFT",y]:
					if (re.match("\d+",x) or x in resolved) and (re.match("\d+",y) or y in resolved):
						p1 = int(x) if x not in resolved else resolved[x]
						p2 = int(y) if y not in resolved else resolved[y]
						resolved[key] = p1 << p2
						wires.pop(key)
					else:
						continue

				case ["NOT",x]:
					if (re.match("\d+",x) or x in resolved):
						p1 = int(x) if x not in resolved else resolved[x]
						resolved[key] = (1 << 16) - 1 - p1
						wires.pop(key)
					else:
						continue

	return resolved["a"]


def part2():
	wires = {line.split(" -> ")[1]:line.split(" -> ")[0] for line in data.splitlines()}
	resolved = {"b":46065}
	wires.pop("b")
	while len(wires):
		for key, value in dict(wires).items():
			match value.split(" "):
				case [x]:
					if re.match("\d+",x) or x in resolved:
						resolved[key] = int(x) if x not in resolved else resolved[x]
						wires.pop(key)
					else:
						continue
			
				case [x,"AND",y]:
					if (re.match("\d+",x) or x in resolved) and (re.match("\d+",y) or y in resolved):
						p1 = int(x) if x not in resolved else resolved[x]
						p2 = int(y) if y not in resolved else resolved[y]
						resolved[key] = p1 & p2
						wires.pop(key)
					else:
						continue

				case [x,"OR",y]:
					if (re.match("\d+",x) or x in resolved) and (re.match("\d+",y) or y in resolved):
						p1 = int(x) if x not in resolved else resolved[x]
						p2 = int(y) if y not in resolved else resolved[y]
						resolved[key] = p1 | p2
						wires.pop(key)
					else:
						continue
					
				case [x,"RSHIFT",y]:
					if (re.match("\d+",x) or x in resolved) and (re.match("\d+",y) or y in resolved):
						p1 = int(x) if x not in resolved else resolved[x]
						p2 = int(y) if y not in resolved else resolved[y]
						resolved[key] = p1 >> p2
						wires.pop(key)
					else:
						continue

				case [x,"LSHIFT",y]:
					if (re.match("\d+",x) or x in resolved) and (re.match("\d+",y) or y in resolved):
						p1 = int(x) if x not in resolved else resolved[x]
						p2 = int(y) if y not in resolved else resolved[y]
						resolved[key] = p1 << p2
						wires.pop(key)
					else:
						continue

				case ["NOT",x]:
					if (re.match("\d+",x) or x in resolved):
						p1 = int(x) if x not in resolved else resolved[x]
						resolved[key] = (1 << 16) - 1 - p1
						wires.pop(key)
					else:
						continue

	return resolved["a"]


if __name__ == '__main__':
	 print(part1())
	 print(part2())