import sys
import random
directions = ['north','south','west','east','up','down']
short_directions = ['n','s','w','e','u','d']
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
        

        
front_gate = Room('Front Gate', 'front_yard', None, None, None, None, \
 None, "You are at the entrance of BuckeBerry, a mysterious new structure that was built ten years without any information and only allows employees in. You could only go north, to the front yard.")

front_yard = Room('Front Yard', 'waiting_room', 'front_gate', 'parking_lot', 'snack_store', None, \
 None, "It is empty here with nobody insight, silence fills the yard as well. There is a snack bar to the east and the parking lot to the west.")
 
snack_store = Room('Snack Store', None, None, None, 'front_yard', None,\
None, "All the products here are gone with a crowbar laying on the ground besides a broken window. The only way out is west, back to the front yard.")

parking_lot = Room('Parking Lot', None, None, None, 'front_yard', None,\
None, "There is a lot of cars here but nobody in sight. The only way out is east, back to the front yard.")

waiting_room = Room('Waiting Room', 'elevator', 'front_yard','office_a', \
'office_b', None, None, 'The waiting room is empty with the source of light flickering on top of you. North of you is an elevator, west of you is an office as well as to the east.') 

office_a = Room('Office A', None, None, None, 'waiting_room', None, \
None, "There is nobody here and it is dark as well. This weird red glowing thing is on the wall. The only way out is back east, the waiting room.")

office_b = Room('Office B', None,None,'waiting_room',None,None,'tunnel1','There is a wierd red glowing thing on the wall and nobody is in here as well. There is also a trapdoor on the ground wide open in to the darkness. To the west is the waiting room and down is a tunnel.')

tunnel1 = Room('Tunnel',None,None,None,'tunnel2','office_b',None,'It is dark, the only light that shines is east as well as the top of you which is an office.' )

tunnel2 = Room('Tunnel',None,None,'tunnel1','tunnel3',None,None,'It is dark, the only light that shines is east.')

tunnel3 = Room('Tunnel',None,None,'tunnel2',None,'labatory',None,'It is dark, the only light that shines is east as well as the top of you which is a mysterious room.')

labatory1 = Room('Labatory','cell_humans','supply_room1','observation1',None,None,'tunnel3','This room is full of beakers and weird chemicals are spilled everywhere. Bits and pieces of the red stuff is on the floor and there is a bucket full of blood. North of you is a cell room, west is a supply room, east is a observation room, and below is the tunnel.')

cells_humans = Room('Human Test Subject Cells','armory1','labatory1','security_system1','test_subjects',None,None,'Some cells are empty but some have the red stuff in it with blood on the ground. There is a camera on the top of each cell and a huge window on the wall so people can see the cells through the observation room. North of you is a armory, south of you is the labatory, west is a security system room, and east is a test subjects room.')

supply_room1 = Room('Supply Room',None,None,None, 'labatory1',None,None,'There are a lot of boxes here and there is a desk with a computer that keeps track of what goes in and out. The red stuff is on or near the boxes. The only way out is east, back to the labatory.')

observation1 = Room('Observation Room',None,None,'labatory1',None,None,None,'There is a big window on the wall that lets you see the cells. There is also a control panel that lets you open certain cells and sound the alarm but you need power. The only way to go is west, back to the labatory.')

security_system1 = Room('Security System Room',None,None, None,'cells_humans',None,None,'There is a bunch of monitors on the wall but some broken or almost completely gone. The only way to go is east, back to the human cells')

armory1 = Room()


node = front_gate
is_alive = True 
while is_alive:
    print node.name
    print node.description
    command = raw_input('> ')
    if command in ['q','quit','exit']:
        sys.exit(0)
        
    if command in short_directions:
        command = directions[short_directions.index(command)]
    try:
        node.move(command)
    except:
            print 'You can\'t go that way'


