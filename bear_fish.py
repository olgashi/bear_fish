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

class Animal():
	def move(self, ecosystem):
		random_move = move_where()

class Fish(Animal):
	pass

class Bear(Animal):

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
		print(type(ecosystem[i]))
		print(type(None))

		if ecosystem[i] == none:
			result.append(i)
	return result

'''Initialize ecosystem'''
fish = Fish()
bear = Bear()
none = None
none_list = []
for i in range(0, 10):
	ecosystem.append(random.choice(fish, bear, none))
	ecosystem_move.append(random.choice(-1, 2, 1))

none_list = update_none_list(ecosystem)
print(none_list)

print(ecosystem_move)
for i in range(0, len(ecosystem_move)):
	'''If animal chose not to stay, then check if the adjasent space they are moving to
	contains the same type of animal'''
	if not ecosystem_move[i]==0:
		if two_of_the_same(ecosystem[i], ecosystem[ecosystem_move[i]]):
			print(f'{ecosystem[i]} wants to move where another {ecosystem[ecosystem_move[i]]} lives.\n')
			
		# else:
			# print(f'{ecosystem[i]} wants to move where {ecosystem[ecosystem_move[i]]} lives. Nice try.\n')
	# else:
	# 	print(f'{ecosystem[i]} chose to stay.\n')






