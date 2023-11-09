#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    A function that adds all unique
    integers in a list (only once for each integer)
    """
    # Use set to keep track of unique elements and sum them up
    ree = set()
    no_re = sum([ree.add(num) or num for num in my_list if num not in ree])
    return no_re
