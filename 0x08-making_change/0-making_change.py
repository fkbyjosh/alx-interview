#!/usr/bin/python3
"""
Making Change - Naive Recursive Solution (for comparison)
This solution may have poor performance on large inputs
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    
    Args:
        coins: List of coin values (integers > 0)
        total: Target amount to make
    
    Returns:
        Fewest number of coins needed to meet total
        0 if total is 0 or less
        -1 if total cannot be met by any number of coins
    """
    if total <= 0:
        return 0

    def helper(remaining):
        if remaining == 0:
            return 0
        if remaining < 0:
            return float('inf')
        
        min_coins = float('inf')
        for coin in coins:
            result = helper(remaining - coin)
            if result != float('inf'):
                min_coins = min(min_coins, result + 1)

        return min_coins

    result = helper(total)
    return -1 if result == float('inf') else result
