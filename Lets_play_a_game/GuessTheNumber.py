# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 10:35:47 2016

@author: james meservy
"""

import random
import math
import GameGlobals

# %%

def play():

    min = 1
    max = random.randint(3,1000)
    max_guesses = math.trunc(math.log(max,2) )
    
    random_number = random.randint(min, max, )    
    # GameGlobals.
       
    intro_message = ("","I am thinking of a number between %d and %d. Can you guess what it is?"\
        % (min, max),"","I'll give you %d tries." %(max_guesses))
    GameGlobals.print_tuple(intro_message)
    
    i = 1
    while i <= max_guesses:
        print ""
            
        i = i + 1
    
        try:
            guess = int(raw_input("Guess the number:   "))
    
            if guess == random_number:
                print "Good job! You guessed the number."
                print "You got it on attempt #%d" % (i - 1)
                break
            elif guess < random_number:
                print "Nice try, but that number is too low."
            elif guess > random_number:
                print "Nice try, but that number is too high."
            else:
                print "Are you sure that is a number between %d and %d?" % \
                    (max, min)
        except:
            print "Are you sure that is a number?"

    if i > max_guesses:
        end_message = ("","Hmm. That was your last try.","",\
        "My number was %d." % (random_number),"","Better luck next time!")        
        
        GameGlobals.print_tuple(end_message)

    print ""
    raw_input("Press <enter> to exit....")
    
if __name__ == "__main__":
    play()
