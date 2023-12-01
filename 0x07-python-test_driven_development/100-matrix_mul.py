"""This module contains a function that multiplies two matrices."""


def matrix_mul(matrix_a, matrix_b):
    """Function to multiply two matrices."""
    if not isinstance(matrix_a, list):
        raise TypeError("matrix_a must be a list")
    if not isinstance(matrix_b, list):
        raise TypeError("matrix_b must be a list")

    """ Variables to verify matrix multiplication compatibility"""
    num_columns_a = 0
    num_rows_b = 0

   """ # Check requirements for matrix_a"""
    if not matrix_a:
        raise ValueError("matrix_a can't be empty")
    for row in matrix_a:
        if not isinstance(row, list):
            raise TypeError("matrix_a must be a list of lists")
        if not row:
            raise ValueError("matrix_a can't contain empty rows")
        if len(row) != len(matrix_a[0]):
            raise TypeError("each row of matrix_a must be of the same size")
        num_columns_a = len(row)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix_a should contain only integers or floats")

   """ # Check requirements for matrix_b"""
    if not matrix_b:
        raise ValueError("matrix_b can't be empty")
    for row in matrix_b:
        if not isinstance(row, list):
            raise TypeError("matrix_b must be a list of lists")
        if not row:
            raise ValueError("matrix_b can't contain empty rows")
        if len(row) != len(matrix_b[0]):
            raise TypeError("each row of matrix_b must be of the same size")
        num_rows_b += 1
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix_b should contain only integers or floats")

  """  # Check if multiplication is possible"""
    if num_columns_a != num_rows_b:
        raise ValueError("matrix_a and matrix_b can't be multiplied")

    multiplied_matrix = []

    for row_a in matrix_a:
        new_row = []
        for i in range(len(matrix_b[0])):
            result = sum(row_a[k] * matrix_b[k][i] for k in range(len(row_a)))
            new_row.append(result)
        multiplied_matrix.append(new_row)

    return multiplied_matrix
