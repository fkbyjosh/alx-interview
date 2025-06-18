#!/usr/bin/python3
'''0x09. Island Perimeter'''
def island_perimeter(grid):
    '''returns the perimeter of the island described in grid'''
    counter = 0
    grid_max = len(grid) - 1  # index of the last list in the grid
    lst_max = len(grid[0]) - 1  # index of the last square in list
    
    # Iterate through each row and column in the grid
    for lst_idx, lst in enumerate(grid):
        for land_idx, land in enumerate(lst):
            # Only process land cells (value = 1)
            if land == 1:
                # Check left and right neighbors
                if land_idx == 0:
                    # At leftmost edge - always add 1 for left side
                    counter += 1
                    # Check right neighbor - add 1 if it's water
                    if lst[land_idx + 1] == 0:
                        counter += 1
                elif land_idx == lst_max:
                    # At rightmost edge - check left neighbor
                    if lst[land_idx - 1] == 0:
                        counter += 1
                    # Always add 1 for right side (grid boundary)
                    counter += 1
                else:
                    # In middle - check both left and right neighbors
                    if lst[land_idx - 1] == 0:
                        counter += 1
                    if lst[land_idx + 1] == 0:
                        counter += 1
                
                # Check top and bottom neighbors
                if lst_idx == 0:
                    # At top edge - always add 1 for top side
                    counter += 1
                    # Check bottom neighbor - add 1 if it's water
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1
                elif lst_idx == grid_max:
                    # At bottom edge - check top neighbor
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1
                    # Always add 1 for bottom side (grid boundary)
                    counter += 1
                else:
                    # In middle - check both top and bottom neighbors
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1
    
    return counter
