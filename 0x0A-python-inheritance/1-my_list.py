#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """
contains the MyList class sub
"""
    def print_sorted(self):
        """initializes the object"""
        sorted_list = sorted(self)
        """prints the sorted list"""
        print(sorted_list)
