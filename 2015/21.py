from aocd import data, submit
from itertools import combinations

def part1():
	weapons = [(8,4,0),(10,5,0),(25,6,0),(40,7,0),(74,8,0)]
	armors = [(0,0,0),(13,0,1),(31,0,2),(53,0,3),(75,0,4),(102,0,5)]
	rings = [(0,0,0),(0,0,0),(25,1,0),(50,2,0),(100,3,0),(20,0,1),(40,0,2),(80,0,3)]
	boss_stats = [int(line.split(' ')[-1]) for line in data.splitlines()]
	boss = unit(*[int(line.split(' ')[-1]) for line in data.splitlines()])
	min_gold = 9999
	for ring_combination in combinations(rings,2):
		for weapon in weapons:
			for armor in armors:
				player = unit(100,armor[1]+weapon[1]+ring_combination[0][1]+ring_combination[1][1],armor[2]+weapon[2]+ring_combination[0][2]+ring_combination[1][2])
				boss = unit(*boss_stats)
				gold = armor[0]+weapon[0]+ring_combination[0][0]+ring_combination[1][0]
				while True:
					boss.hp -= player.dmg - boss.armor if player.dmg - boss.armor > 0 else 1
					if boss.hp <= 0:
						min_gold = min(min_gold,gold)
						break
					player.hp -= boss.dmg - player.armor if boss.dmg - player.armor > 0 else 1
					if player.hp <= 0:
						break
	return min_gold

def part2():
	weapons = [(8,4,0),(10,5,0),(25,6,0),(40,7,0),(74,8,0)]
	armors = [(0,0,0),(13,0,1),(31,0,2),(53,0,3),(75,0,4),(102,0,5)]
	rings = [(0,0,0),(0,0,0),(25,1,0),(50,2,0),(100,3,0),(20,0,1),(40,0,2),(80,0,3)]
	boss_stats = [int(line.split(' ')[-1]) for line in data.splitlines()]
	boss = unit(*[int(line.split(' ')[-1]) for line in data.splitlines()])
	max_gold = 0
	for ring_combination in combinations(rings,2):
		for weapon in weapons:
			for armor in armors:
				player = unit(100,armor[1]+weapon[1]+ring_combination[0][1]+ring_combination[1][1],armor[2]+weapon[2]+ring_combination[0][2]+ring_combination[1][2])
				boss = unit(*boss_stats)
				gold = armor[0]+weapon[0]+ring_combination[0][0]+ring_combination[1][0]
				while True:
					boss.hp -= player.dmg - boss.armor if player.dmg - boss.armor > 0 else 1
					if boss.hp <= 0:
						break
					player.hp -= boss.dmg - player.armor if boss.dmg - player.armor > 0 else 1
					if player.hp <= 0:
						max_gold = max(max_gold,gold)
						break
	return max_gold

class unit():
	def __init__(self, hp, dmg, armor):
		self.hp = hp
		self.dmg = dmg
		self.armor = armor


if __name__ == '__main__':
	print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	submit(part2())