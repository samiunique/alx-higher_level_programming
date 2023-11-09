#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    A function that replaces all occurrences
    of an element by another in a new list
    """
    # Use list comprehension to create a new list with replacements
    new_list = [replace if elem == search else elem for elem in my_list]
    return new_list
