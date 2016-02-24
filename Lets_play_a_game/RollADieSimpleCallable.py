# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:38:01 2016

@author: james meservy
"""

import random

# Define function
# Set default values for variables

def validate_num_sides(num_sides, min_num_sides, max_num_sides):
    if num_sides < min_num_sides or num_sides > max_num_sides:
        print "That's a silly answer. Let's try that again."
        print ""
        return False
    else:
        print "%d sides it is." % num_sides
        print ""
        return True

# %%
def play():
   
    
    print ""
    print "Let's roll a die!"
    print ""
    
    
    # Add data validation step
    while go_again == "Y" or go_again == "y":
        while num_sides_valid is False:
            error_text = ("", "Are you sure that was a number?", "",\
            "Let's try that again.", "")
    
            try:
                num_sides = input("How many sides would you like the die to have?    ")        
                print ""
                num_sides_valid = validate_num_sides(num_sides, min_num_sides, max_num_sides)
            except ValueError or SyntaxError:
                for text in error_text:
                    print text
                num_sides_valid = False
            except NameError:
                for text in error_text:
                    print text
                num_sides_valid = False
           
    # %%
    
        result = random.randint(1, num_sides)
    
        print raw_input("<press enter to roll the die>")
        print "The roll is %d." % (result)
        print ""
        print raw_input("<press enter>")    
        print "Would you like to roll the die again?"
        print ""
        answer = raw_input('Type "Y" to play again. Type anything else to quit.  ')
        go_again = "%s" % (answer)
    
    print ""
    print "Thanks for playing!"

if __name__ == "__main__":
    num_sides_valid = False
    go_again = "Y"
    min_num_sides = 3
    max_num_sides = 100 
    play()
