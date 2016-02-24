# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 17:51:13 2016

@author: james meservy
"""

standard_input_errors = (ValueError, NameError, SyntaxError) 

def print_tuple(text_to_print):
    for text in text_to_print:
        print text
    
def user_press_enter(prompt = "<press enter>"):
    print raw_input(prompt) 
        