#!/usr/bin/python3
"""
N Queens Problem Solver
"""

import sys


def is_safe(positions, row, col):
    """
    Check if a queen can be placed at position (row, col)
    given the current positions of other queens
    """
    for i in range(row):
        # Check if queens are in same column or diagonal
        if positions[i] == col or \
           positions[i] - i == col - row or \
           positions[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    """
    Solve N Queens problem and return all solutions
    """
    solutions = []
    positions = [0] * n
    
    def backtrack(row):
        if row == n:
            # Found a solution
            solution = []
            for i in range(n):
                solution.append([i, positions[i]])
            solutions.append(solution)
            return
        
        for col in range(n):
            if is_safe(positions, row, col):
                positions[row] = col
                backtrack(row + 1)
    
    backtrack(0)
    return solutions


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
