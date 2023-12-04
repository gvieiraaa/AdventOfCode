from aocd import data, submit
import hashlib

def part1():
	for i in range(100_000_000):
		md5 = hashlib.md5(f"{data}{i}".encode('utf-8')).hexdigest()
		if md5[0:5] == "0" * 5:
			submit(i)
			break


def part2():
	for i in range(100_000_000):
		md5 = hashlib.md5(f"{data}{i}".encode('utf-8')).hexdigest()
		if md5[0:6] == "0" * 6:
			submit(i)
			break

if __name__ == '__main__':
	#part1()
	part2()