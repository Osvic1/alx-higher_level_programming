#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """returns a new dictionary with"""
    """all values multiplied by 2"""
    for x in a_dictionary:
        new_dict = {x: (a_dictionary[x] * 2)}
    return new_dict
