0x07. Rotate 2D Matrix

## Description

This project implements an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. The solution demonstrates efficient matrix manipulation techniques using Python, focusing on space optimization by performing the rotation without creating additional data structures.

## Algorithm Explanation

The rotation is achieved through a two-step process:

1. **Matrix Transposition**: Swap elements across the main diagonal (matrix[i][j] ↔ matrix[j][i])
2. **Row Reversal**: Reverse each row of the transposed matrix

### Visual Example

Original Matrix:
```
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
```

After Transposition:
```
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
```

After Row Reversal (Final Result):
```
[7, 4, 1]
[8, 5, 2]
[9, 6, 3]
```

## Key Concepts

- **In-place Operations**: Modifying the matrix without using additional space
- **Matrix Transposition**: Swapping rows and columns
- **Space Complexity**: O(1) - constant space usage
- **Time Complexity**: O(n²) - quadratic time for n x n matrix

## Requirements

- **Environment**: Ubuntu 20.04 LTS with Python 3.8.10
- **Style**: Code follows pycodestyle (version 2.8.0)
- **Documentation**: All functions and modules are documented
- **Restrictions**: No module imports allowed
- **File Structure**: Executable files with proper shebang

## Files

- `0-rotate_2d_matrix.py`: Main implementation file
- `README.md`: Project documentation
- `main_0.py`: Test file (example usage)

## Usage

```python
#!/usr/bin/python3
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)
print(matrix)
# Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

## Function Prototype

```python
def rotate_2d_matrix(matrix):
    """
    Rotate an n x n 2D matrix 90 degrees clockwise in-place.
    
    Args:
        matrix (list[list[int]]): Square 2D matrix to rotate
        
    Returns:
        None: Matrix is modified in-place
    """
```

## Testing

To test the implementation:

1. Make the file executable: `chmod +x 0-rotate_2d_matrix.py`
2. Run the test: `./main_0.py`

Expected output:
```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Algorithm Complexity

- **Time Complexity**: O(n²) where n is the matrix dimension
- **Space Complexity**: O(1) as no additional space is used

## Author

Joshua Baka
