#!/usr/bin/python3
"""A module to divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """ Function that divides the integer/float numbers of a matrix
    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix
    Returns:
        A new matrix with the result of the division
    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size
        ZeroDivisionError: If div is zero
    """
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')


    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(msg_type)

    if all(isinstance(e, (int, float)) for r in matrix for e in r) is False:
        raise TypeError(msg_type)

    if div == 0:
        raise ZeroDivisionError('division by zero')

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return(new_matrix)
