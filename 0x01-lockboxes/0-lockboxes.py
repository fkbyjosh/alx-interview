#!/usr/bin/python3


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    '''
    n = len(boxes)
    if n == 0:
        return True
    
    # Keep track of boxes we can open
    unlocked = [False] * n
    unlocked[0] = True  # Box 0 is unlocked by default
    
    # Keys we have access to
    keys = boxes[0].copy()
    
    # Try to open new boxes
    while keys:
        key = keys.pop()
        
        # If key is valid and box is not already unlocked
        if 0 <= key < n and not unlocked[key]:
            unlocked[key] = True
            # Add new keys from this box
            keys.extend([k for k in boxes[key] if not unlocked[k]])
    
    # Check if all boxes are unlocked
    return all(unlocked)
