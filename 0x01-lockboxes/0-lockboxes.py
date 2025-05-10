#!/usr/bin/python3
"""
Module for determining if all locked boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened

    Args:
        boxes (list of lists): A list of boxes where each box may contain
                              keys to other boxes

    Returns:
        bool: True if all boxes can be opened, False otherwise
    """
    n = len(boxes)
    # Keep track of which boxes we can open
    unlocked = [False] * n
    unlocked[0] = True  # First box is already unlocked

    # Stack to keep track of keys to process
    keys_to_check = [0]  # Start with the first box

    while keys_to_check:
        current_box = keys_to_check.pop()

        # Check each key in the current box
        for key in boxes[current_box]:
            # If the key opens a box we haven't unlocked yet
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys_to_check.append(key)

    # Check if all boxes are unlocked
    return all(unlocked)
