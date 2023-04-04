#!/usr/bin/python3
""" function that divides all elements of a matrix. """
def matrix_divided(matrix, div):
    dividedMatrix = []
    if not isinstance(matrix, (int, float, list)):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int,float)):
        raise TypeError('div must be a number')
    if(div == 0):
        raise ZeroDivisionError('division by zero')
    for row in matrix:
        for elem in row:
            dividedMatrix.append(round(elem/div, 2))
                    
    return [dividedMatrix]
