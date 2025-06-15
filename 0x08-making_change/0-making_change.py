#!/usr/bin/python3
"""Module to find the fewest number of coins needed to meet a given total"""


def makeChange(coins, total):
    """Determine the minimum number of coins to make up a total"""
    if total <= 0:
        return 0
    if not coins:
        return -1

    # Initialize dp array with inf values
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
