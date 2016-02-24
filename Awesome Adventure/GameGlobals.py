# -*- coding: utf-8 -*-
"""
Defines global functions for the Awesome Adventure game.

Created on Sat Jan 16 13:30:05 2016

@author: James Meservy
"""


standard_input_errors = (ValueError, NameError, SyntaxError) 

def print_tuple(text_to_print):
    for text in text_to_print:
        print ""        
        print text
        print ""
        
def print_tuple_no_spaces(text_to_print):
    for text in text_to_print:
        print text    
    
    
def user_press_enter(prompt = "<press enter>"):
    print raw_input(prompt) 