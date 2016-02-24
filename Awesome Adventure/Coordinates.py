# -*- coding: utf-8 -*-
"""
Declare functions for moving and setting location coordinates.

Created on Sat Jan 16 13:31:12 2016

@author: James Meservy
"""
import operator
import GameGlobals

# %%


position = [0,0]
move_distance = {"Forward" : [0,1], "Back" : [0,-1], \
"Left" : [-1,0], "Right" : [1,0]}

def move_4_times(position):
    for i in (1,2,3,4):
        print ""    
        print "This is move #%d." % (i)    
        position = move(position)
        print ""
        print "Your new position is %s." %(str(position))
    return position

def move(position):
    move_direction = raw_input("Would you like to move forward, back, left, or right?       ")    
    
    #first if statement is causing an error.
    if move_direction == "forward" or move_direction =="f":
        move_vector = (0,1)
    elif move_direction == "back":
        move_vector = (0,-1)
    elif move_direction == "left":
        move_vector = (-1,0)
    elif move_direction == "right":
        move_vector = (1,0)
    else:
        move_vector = ""
        
    new_position = map(operator.add,position, move_vector)
    return new_position
 

def check_position():
    x = position[0]
    y = position [1]
    is_position_valid = bool(not game_map[x][y])
    return is_position_valid
 
  
position = move_4_times(position)
GameGlobals.user_press_enter()
print check_position()



 
  

# %%
    
    
game_map = [[0,0,0,0],
            [1,1,1,1],
            [1,1,0,0],
            [0,0,1,1]
            ]
    
game_map[1][1]
   

#def give_user_options()    

    
# map(operator.add,[1,1],[2,1])