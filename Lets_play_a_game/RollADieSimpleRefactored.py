# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:38:01 2016

@author: james meservy
"""

import random
import GameGlobals

# %%

# Define functions

#Somehow it seems to be exiting the loop even when user gives incorrect input


def ask_num_sides():            
            num_sides_valid = False            
            while num_sides_valid is False:
                try:
                    response = input(
                    "How many sides would you like the die to have?    ")        
                    print ""
                    num_sides_valid = validate_num_sides(response)
                    return response
        # Not getting value errors, because input allows string as a function
                except GameGlobals.standard_input_errors:
                    error_text = ("", "Are you sure that was a number?", "",\
                    "Let's try that again.", "")
                    GameGlobals.print_tuple(error_text)
                    num_sides_valid = False
                                        
def validate_num_sides(num_sides):
        min_num_sides = 3
        max_num_sides = 100
        
        if num_sides < min_num_sides or num_sides > max_num_sides:
            print ""            
            print "That's a silly answer. Let's try that again."
            print ""
            return False
        else:
            print "%d sides it is." % num_sides
            print ""
            return True
 
def roll_die(num_sides):        

    roll_result = random.randint(1, num_sides)      
   
    GameGlobals.user_press_enter("<press enter to roll the die>")
    print "The roll is %d." % (roll_result)
    print ""
    GameGlobals.user_press_enter()   

             
def ask_if_go_again():
    print "Would you like to roll the die again?"
    print ""
    answer = raw_input('Type "Y" to play again. Type anything else to quit.  ')
    return "%s" % (answer)               
 
    
   # %%
#Run program              


def play():    
    
    intro_message = ("", "Let's roll a die!", "")
    GameGlobals.print_tuple(intro_message)
    
    num_sides = ask_num_sides()
    
    go_again = "Y"     
    while go_again == "Y" or go_again == "y":
        roll_die(num_sides)
        go_again = ask_if_go_again()
    
    print ""
    print "Thanks for playing!"

if __name__ == "__main__":
    play()
    