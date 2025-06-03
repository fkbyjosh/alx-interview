#!/usr/bin/python3
"""
Module for rotating a 2D matrix 90 degrees clockwise in-place.

This module provides functionality to rotate an n x n 2D matrix by 90 degrees
clockwise using matrix transposition and row reversal.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate an n x n 2D matrix 90 degrees clockwise in-place.

    Algorithm: First transpose the matrix, then reverse each row.
    Time complexity: O(n²), Space complexity: O(1).

    Args:
        matrix (list[list[int]]): Square 2D matrix to be rotated in-place.

    Returns:
        None: Matrix is modified in-place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix (swap elements across main diagonal)
    for i in range(n):
        for j in range(i + 1, n):
            # Swap matrix[i][j] with matrix[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row to complete the 90-degree clockwise rotation
    for i in range(n):
        matrix[i].reverse()
