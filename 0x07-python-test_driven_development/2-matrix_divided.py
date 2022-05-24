#!/usr/bin/python3
"""
Module to divide a given matrix

Arugments: matrix, div
"""


def matrix_divided(matrix, div):
    """Function divides all elements of a matrix
    Returns: The divided matrix
    """
    if all(isinstance(ele, list) for ele in matrix) is False:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    
    for row in matrix:
        for ele in row:
            if type(ele) is not int and type(ele) is not float:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

    if type(div) is int or type(div) is float:
        if div == 0:
            raise ZeroDivisionError('division by zero')
    else:
        raise TypeError('div must be a number')

    matrixDiv = list(map(lambda row: [round(ele / div, 2) for ele in row], matrix))
    return matrixDiv
