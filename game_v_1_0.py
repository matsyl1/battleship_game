# imports
import random
import numpy as np

# NEW: user input for grid size (max 18*) and nr of boats (max 9*). *Numpy display limitations.
grid_size = int(input("Select the grid size (max 18): "))
nr_of_boats = int(input("Select the nr of boats (max 9): ")) + 1

# grid
grid = np.full([grid_size, grid_size], ".", dtype=str)

# FUNCTIONS--------------------------------------------------------------------------------------
# check for boat overlap
def overlap(boat_coords, new_coords):
    for i in boat_coords:
        if i in new_coords:
            return True
    else:
        return False

# create boat coords (start/end)
def create_boat_coords(size, used_coords):
    while True:
        x1, y1 = random.randint(0, grid_size - size), random.randint(0, grid_size - size)
        # boat direction (horizontal/vertical)
        if random.choice([True, False]):
            (x2, y2) = x1 + size - 1, y1
        else:
            (x2, y2) = x1, y1 + size - 1

        # boat coords (middle)
        new_coords = [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]
        if not overlap(used_coords, new_coords):
            return [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]

# NEW: generate boats
def generate_boats():
    # empty list to track used coords
    used_coords = []
    # loop thru boats
    for size in range(nr_of_boats):
        boat = create_boat_coords(size, used_coords)
        for (x, y) in boat:
            grid[y, x] = size
        # extend list of used coords
        used_coords.extend(boat)
    print(grid)
    print(used_coords)

generate_boats()