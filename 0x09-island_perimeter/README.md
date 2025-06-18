Island Perimeter

Calculate the perimeter of an island represented in a 2D grid.

## Problem

Given a grid where `0` represents water and `1` represents land, calculate the perimeter of the island.

## Requirements

- Grid is a list of lists of integers (0 or 1)
- Each cell is a unit square
- Cells connect horizontally/vertically only
- Grid dimensions ≤ 100x100
- Grid is surrounded by water
- Contains at most one island
- No interior lakes

## Function Signature

```python
def island_perimeter(grid):
    """Returns the perimeter of the island in grid"""
```

## Example

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
```

## Files

- `0-island_perimeter.py` - Main implementation
- `0-main.py` - Test file

## Repository

- **GitHub**: `alx-interview`
- **Directory**: `0x09-island_perimeter`
