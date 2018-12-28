'''Ecosystem contains a bear and fish. 
The ecosystem consists of a river which is a large list.
Each element of the list is either Bear object, Fish object or None.
Each time step, based on a random process an animal either attempts to
move to adjacent list location or stay where they are. 
If two animals of the same type try to move into the same cell, 
they stay where they are but create a new instance of that type of animal, 
which is placed in a random empty (None) location in the list.
If bear and fish collide then bear eats the fish.'''
import random


ecosystem = []
pick_move = [ -1, 0, 1]
ecosystem_move = []

class Fish():
	pass

class Bear():

	def is_fish(self, other):
		instance(other, Fish)

	def eat_fish(self, Fish):
		pass

def move_where():
	return random.randrange(-1, 2, 1)

def two_of_the_same(one, other):
		if one == other:
			return True
		else:
			return False
def update_none_list(ecosystem):
	none = None
	result = []
	for i in range(0,len(ecosystem)):
		if ecosystem[i] == none:
			result.append(i)
	return result

'''Instance variables to populate a list with choice of animals'''
fish = Fish()
bear = Bear()
none = None
random_animal = [fish, bear, none]

'''Set number of animals in ecosystem'''
n = 10

'''To take note of positions where no animal lives (None type)'''
none_list = []

'''Start with initializing ecosystem and animals deciding 
to move in the same iteration ----> as a TEST. Change timing of moves later'''
for i in range(0, n+1):
	ecosystem.append(random.choice(random_animal))
	ecosystem_move.append(random.choice(pick_move))
'''Indices of where no animal lives'''
none_list = update_none_list(ecosystem)

'''Each animal moves/stays'''
for i in range(0, len(ecosystem_move)):
	'''If animal chose not to stay, then check if the adjasent space they are moving to
	contains the same type of animal'''
	if not ecosystem_move[i] == 0 and not ecosystem[i] == None:
		if two_of_the_same(ecosystem[i], ecosystem[ecosystem_move[i]]):
			print(f'{ecosystem[i]} wants to move where another {ecosystem[ecosystem_move[i]]} lives.\n')
			'''If two of the same time, want to move to the same location, new animal of the same kind is created
			and placed in a random "None' location'''

			new_animal = type(ecosystem[i])
			# print('---->', new_animal)
			# print(ecosystem)
			if len(none_list) > 0:
				new_animal_space = random.choice(none_list)
				ecosystem[new_animal_space] = new_animal
				# print(ecosystem)
			else:
				ecosystem.append(new_animal)

		else:
			# print(f'{ecosystem[i]} wants to move where {ecosystem[ecosystem_move[i]]} lives. Nice try.\n')
			if isinstance(ecosystem[i], Bear) and isinstance(ecosystem[ecosystem_move[i]], Fish):
				print(ecosystem)
				ecosystem[i] = None
				ecosystem[ecosystem_move[i]] = Bear()
				print(f'Bear {ecosystem[i]} ate fiss {ecosystem[ecosystem_move[i]]}.')
				print(ecosystem)
	else:
		'''Animal chose to stay'''
		print(f'{ecosystem[i]} chose to stay.\n')
	none_list = update_none_list(ecosystem)