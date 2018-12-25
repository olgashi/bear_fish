'''Ecosystem contains a bear and fish. 
The ecosystem consists of a river which a large list.
Each element of the list is either Bear object, Fish object or None.
Each time step, based on a random process an animal either attempts to
move to adjacent list location or stay where they are. 
If two animals of the same type
try to move into the same cell, they stay where they are but create a new instance of 
that type of animal, which is placed in a random empty (None) location in the list.
If bear and fish collide then bear eats the fish.'''
import random


ecosystem = []
pick_move = [ -1, 0, 1]

class Animal():
	def move_where(self):
		random.randrange(-1, 2, 1)


class Fish(Animal):
	pass

class Bear(Animal):

	def is_fish(self, other):
		instance(other, Fish)

	def eat_fish(self, other):


for i in range(0, 21):
	ecosystem.append(random.sample((Fish(), Bear(), None), 1))







