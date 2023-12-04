from aocd import data, submit
import random

"""Magic Missile costs 53 mana. It instantly does 4 damage.
Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana."""

def part1():
	input = [int(line.split(' ')[-1]) for line in data.splitlines()]
	min_mana = 999999
	for _ in range(5_000_000):
		mana_spent = 0
		boss_instance = ''
		player_instance = ''
		#boss_instance = boss(*input)
		boss_instance = boss(71,10)
		player_instance = player(50,500)
		# boss_instance = boss(14,8)
		# player_instance = player(10,250)
		while True:
			# player turn
			if player_instance.shield['turns_left'] == 1:
				player_instance.armor = 0
			if player_instance.shield['turns_left'] > 0:
				player_instance.shield['turns_left'] -= 1
			if player_instance.poison['turns_left'] > 0:
				player_instance.poison['turns_left'] -= 1
				boss_instance.hp -= player_instance.poison['damage']
			if player_instance.recharge['turns_left'] > 0:
				player_instance.recharge['turns_left'] -= 1
				player_instance.mana += player_instance.recharge['mana']

			#check death
			if player_instance.hp <= 0:
				break
			if boss_instance.hp <= 0:
				min_mana = min(min_mana,mana_spent)
				break
			
			attack_choices = [0]
			if player_instance.mana < 53:
				break
			if player_instance.mana >= player_instance.drain['cost']:
				attack_choices.append(1)
			if player_instance.mana >= player_instance.shield['cost'] and player_instance.shield['turns_left'] == 0:
				attack_choices.append(2)
			if player_instance.mana >= player_instance.poison['cost'] and player_instance.poison['turns_left'] == 0:
				attack_choices.append(3)
			if player_instance.mana >= player_instance.recharge['cost'] and player_instance.recharge['turns_left'] == 0:
				attack_choices.append(4)

			# attack
			match random.choice(attack_choices):
				case 0: # missile
					mana_spent += player_instance.missile['cost']
					player_instance.mana -= player_instance.missile['cost']
					boss_instance.hp -= player_instance.missile['damage']
				case 1: # drain
					mana_spent += player_instance.drain['cost']
					player_instance.mana -= player_instance.drain['cost']
					boss_instance.hp -= player_instance.drain['damage']
					player_instance.hp += player_instance.drain['heal']
				case 2: # shield
					mana_spent += player_instance.shield['cost']
					player_instance.mana -= player_instance.shield['cost']
					player_instance.armor += player_instance.shield['armor']
					player_instance.shield['turns_left'] = player_instance.shield['turns']
				case 3: # poison
					mana_spent += player_instance.poison['cost']
					player_instance.mana -= player_instance.poison['cost']
					#boss_instance.hp -= player_instance.poison['damage']
					player_instance.poison['turns_left'] = player_instance.poison['turns']
				case 4: # recharge
					mana_spent += player_instance.recharge['cost']
					player_instance.mana -= player_instance.recharge['cost']
					player_instance.recharge['turns_left'] = player_instance.recharge['turns']

			#check death
			if player_instance.hp <= 0:
				break
			if boss_instance.hp <= 0:
				min_mana = min(min_mana,mana_spent)
				break

			# boss turn
			if player_instance.shield['turns_left'] == 1:
				player_instance.armor = 0
			if player_instance.shield['turns_left'] > 0:
				player_instance.shield['turns_left'] -= 1
			if player_instance.poison['turns_left'] > 0:
				player_instance.poison['turns_left'] -= 1
				boss_instance.hp -= player_instance.poison['damage']
			if player_instance.recharge['turns_left'] > 0:
				player_instance.recharge['turns_left'] -= 1
				player_instance.mana += player_instance.recharge['mana']

			#check death
			if player_instance.hp <= 0:
				break
			if boss_instance.hp <= 0:
				min_mana = min(min_mana,mana_spent)
				break

			player_instance.hp -= max(boss_instance.damage - player_instance.armor,1)

			#check death
			if player_instance.hp <= 0:
				break
			if boss_instance.hp <= 0:
				min_mana = min(min_mana,mana_spent)
				break

	return min_mana

def part2():
	input = [int(line.split(' ')[-1]) for line in data.splitlines()]
	min_mana = 999999
	for _ in range(5_000_000):
		mana_spent = 0
		boss_instance = ''
		player_instance = ''
		#boss_instance = boss(*input)
		boss_instance = boss(71,10)
		player_instance = player(50,500)
		# boss_instance = boss(14,8)
		# player_instance = player(10,250)
		while True:

			# player turn
			player_instance.hp -= 1

			#check death
			if player_instance.hp <= 0:
				break

			if player_instance.shield['turns_left'] == 1:
				player_instance.armor = 0
			if player_instance.shield['turns_left'] > 0:
				player_instance.shield['turns_left'] -= 1
			if player_instance.poison['turns_left'] > 0:
				player_instance.poison['turns_left'] -= 1
				boss_instance.hp -= player_instance.poison['damage']
			if player_instance.recharge['turns_left'] > 0:
				player_instance.recharge['turns_left'] -= 1
				player_instance.mana += player_instance.recharge['mana']

			#check death
			if player_instance.hp <= 0:
				break
			if boss_instance.hp <= 0:
				min_mana = min(min_mana,mana_spent)
				break
			
			attack_choices = [0]
			if player_instance.mana < 53:
				break
			if player_instance.mana >= player_instance.drain['cost']:
				attack_choices.append(1)
			if player_instance.mana >= player_instance.shield['cost'] and player_instance.shield['turns_left'] == 0:
				attack_choices.append(2)
			if player_instance.mana >= player_instance.poison['cost'] and player_instance.poison['turns_left'] == 0:
				attack_choices.append(3)
			if player_instance.mana >= player_instance.recharge['cost'] and player_instance.recharge['turns_left'] == 0:
				attack_choices.append(4)

			# attack
			match random.choice(attack_choices):
				case 0: # missile
					mana_spent += player_instance.missile['cost']
					player_instance.mana -= player_instance.missile['cost']
					boss_instance.hp -= player_instance.missile['damage']
				case 1: # drain
					mana_spent += player_instance.drain['cost']
					player_instance.mana -= player_instance.drain['cost']
					boss_instance.hp -= player_instance.drain['damage']
					player_instance.hp += player_instance.drain['heal']
				case 2: # shield
					mana_spent += player_instance.shield['cost']
					player_instance.mana -= player_instance.shield['cost']
					player_instance.armor += player_instance.shield['armor']
					player_instance.shield['turns_left'] = player_instance.shield['turns']
				case 3: # poison
					mana_spent += player_instance.poison['cost']
					player_instance.mana -= player_instance.poison['cost']
					#boss_instance.hp -= player_instance.poison['damage']
					player_instance.poison['turns_left'] = player_instance.poison['turns']
				case 4: # recharge
					mana_spent += player_instance.recharge['cost']
					player_instance.mana -= player_instance.recharge['cost']
					player_instance.recharge['turns_left'] = player_instance.recharge['turns']

			#check death
			if player_instance.hp <= 0:
				break
			if boss_instance.hp <= 0:
				min_mana = min(min_mana,mana_spent)
				break

			# boss turn
			if player_instance.shield['turns_left'] == 1:
				player_instance.armor = 0
			if player_instance.shield['turns_left'] > 0:
				player_instance.shield['turns_left'] -= 1
			if player_instance.poison['turns_left'] > 0:
				player_instance.poison['turns_left'] -= 1
				boss_instance.hp -= player_instance.poison['damage']
			if player_instance.recharge['turns_left'] > 0:
				player_instance.recharge['turns_left'] -= 1
				player_instance.mana += player_instance.recharge['mana']

			#check death
			if player_instance.hp <= 0:
				break
			if boss_instance.hp <= 0:
				min_mana = min(min_mana,mana_spent)
				break

			player_instance.hp -= max(boss_instance.damage - player_instance.armor,1)

			#check death
			if player_instance.hp <= 0:
				break
			if boss_instance.hp <= 0:
				min_mana = min(min_mana,mana_spent)
				break

	return min_mana

class unit:
	def __init__(self,hp):
		self.hp = hp
		self.armor = 0
	
class player(unit):
	def __init__(self,hp,mana):
		super().__init__(hp)
		self.mana = mana
		self.missile = {'cost':53,'damage':4}
		self.drain = {'cost':73,'damage':2,'heal':2}
		self.shield = {'cost':113,'armor':7,'turns':6,'turns_left':0}
		self.poison = {'cost':173,'damage':3,'turns':6,'turns_left':0}
		self.recharge = {'cost':229,'mana':101,'turns':5,'turns_left':0}

class boss(unit):
	def __init__(self,hp,damage):
		super().__init__(hp)
		self.damage = damage

if __name__ == '__main__':
	#print(f"Part 1: {part1()}")
	#submit(part1())
	print(f"Part 2: {part2()}")
	#submit(part2())