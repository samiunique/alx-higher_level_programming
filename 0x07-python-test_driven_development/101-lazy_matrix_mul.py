#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines a matrix multiplication function without using NumPy."""


def matrix_multiplication(m_a, m_b):
    """Multiply two matrices."""
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Both inputs must be lists")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("Both inputs must be lists of lists")

    if len(m_a) == 0 or len(m_b) == 0 or any(len(row) == 0 for row in m_a) or any(len(row) == 0 for row in m_b):
        raise ValueError("Both matrices can't be empty")

    rows_a, cols_a = len(m_a), len(m_a[0])
    rows_b, cols_b = len(m_b), len(m_b[0])

    if cols_a != rows_b:
        raise ValueError("Cannot multiply matrices with these dimensions")

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
