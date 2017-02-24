import sys
import random
class Room():
    def __init__(self, the_name, N, S, E, W, U, D, the_description):
        self.name = the_name
        self.description = the_description
        self.north = N
        self.south = S
        self.west = W
        self.east = E
        self.up = U
        self.down = D 
    def move(self,direction):
        '''This function allows movement to a different node.
        '''
        global node 
        node = globals()[getattr(self, direction)]
crowbar_attack = random.randint(1,20)
class Crowbar():
    def __init__(self,name):
        self.name = name 
        self.attack = crowbar_attack
        self.durability = 100
    def attack(self,name):
        self.attack
        self.durability = -8
        print "You did %d damage!" %self.attack
my_crowbar = Crowbar('Antonio\'s Crowbar')
        
front_gate = Room('Front Gate', 'front_yard', None, None, None, None, \
 None, "You are at the entrance of BuckeBerry, a mysterious new structure that was built ten years without any information and only allows employees in. You could only go north, to the front yard.")

front_yard = Room('Front Yard', 'waiting_room', 'front_gate', 'parking_lot', 'snack_store', None, \
 None, "It is empty here with nobody insight, silence fills the yard as well. There is a snack bar to the east and the parking lot to the west.")
 
snack_store = Room('Snack Store', None, None, None, 'front_yard', None,\
None, "All the products here are gone with a crowbar laying on the ground besides a broken window. The only way out is west, back to the front yard.")

parking_lot = Room('Parking Lot', None, None, None, 'front_yard', None,\
None, "There is a lot of cars here but nobody in sight. The only way out is east, back to the front yard.")

waiting_room = Room('Waiting Room', 'elevator', 'front_yard','office_a', \
'office_b', None, None, 'The waiting room is empty with the ')

office_a = Room('Office A', None, None, None, 'waiting_room', None, \
None, "rojnforinf")

office_b = Room('Office B', None,None,None,None,None,None,'ddff')

node = front_gate




