#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    A function that computes the square value of all integers in a matrix.
    """
    # Use list comprehension to square each element in each column
    new_matrix = [[x**2 for x in col] for col in matrix]
    
    return new_matrix

