# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:44:10 2016

@author: james meservy
"""
import random
import GameGlobals
import RollADieSimpleRefactored
import GuessTheNumber




# %%

if __name__ == "__main__":
    
    intro_text = ("Let's play a game!", "", "Which game would you like to play?", "")

    games = ("1: Roll a Die", "2: Guess The Number","")
    gamenames = ("",RollADieSimpleRefactored, GuessTheNumber)

    GameGlobals.print_tuple(intro_text)
    GameGlobals.print_tuple(games)



    try:
        game = input("Type the number of the game you wish to play, then hit <enter>   ")
        if game <= 0 or game >= len(gamenames): raise ValueError    
    except GameGlobals.standard_input_errors:
        error_text = ("",
        "Come on silly, all you have to do is pick one of the numbers I gave you!",
        "","Oh well, I guess I will just have to pick for you.","")
        GameGlobals.print_tuple(error_text)
        game = random.randint(1,2)
    
    print "You chose %s" %str(games[game - 1])
    print ""
    
    gamenames[game].play()
    
