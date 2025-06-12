0x08. Making Change

## Description
Determine the fewest number of coins needed to meet a given amount using dynamic programming.

## Problem
Given a pile of coins of different values, find the minimum number of coins required to make a specific total amount.

## Requirements
- Return the fewest number of coins needed
- Return `0` if total is 0 or less
- Return `-1` if total cannot be made with available coins
- Assume infinite supply of each coin denomination

## Usage
```python
makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))    # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))    # Output: -1
```

## Algorithm
Dynamic programming approach with O(total × coins) time complexity.

## Files
- `0-making_change.py` - Main solution
- `0-main.py` - Test file

## Repository
- **GitHub repository**: `alx-interview`
- **Directory**: `0x08-making_change`
