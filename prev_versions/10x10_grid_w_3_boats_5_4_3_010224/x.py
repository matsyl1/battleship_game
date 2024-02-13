# imports
import random
import numpy as np


# original grid
grid = np.full([10, 10], ".", dtype=str)


# check that boats don't overlap
# boats_coords = list of coords for existing boat
# new_coords = list of coords considered for new boat
def intersect(boat_coords, new_coords):
    # use for loop to iterate through each coord
    for coord in boat_coords:
        # find coords for boats present in new_coords
        if coord in new_coords:
            return True
    return False


# generate boat coords
# x1, y1 = starting coords of boats and x2, y2 = ending coords of boats

def boat_coords(size, used_coords):
    while True:
        # generate start and end coords for the boat
        x1, y1 = random.randint(0, 10 - size), random.randint(0, 10 - size)
        # random choice
        if random.choice([True, False]):
            # H boat
            x2, y2 = x1 + size - 1, y1
        else:
            # V boat
            x2, y2 = x1, y1 + size - 1

        # test if the generated coordinates overlap with used_coords
        new_coords = [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]
        if not intersect(used_coords, new_coords):
            return [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]


# generate coords for boat 5
boat5_coords = boat_coords(5, [])
for x, y in boat5_coords:
    grid[y, x] = "5"

# update used_coords with boat 5 coords
used_coords = boat5_coords[:]

# generate coords for boat 4
boat4_coords = boat_coords(4, used_coords)
for x, y in boat4_coords:
    grid[y, x] = "4"

# update used_coords with boat 5 coords
used_coords.extend(boat4_coords)

# generate coords for boat 3
boat3_coords = boat_coords(3, used_coords)
for x, y in boat3_coords:
    grid[y, x] = "3"

# update used_coords with boat 5 coords
used_coords.extend(boat3_coords)

# generate coords for boat 2
boat3_coords = boat_coords(2, used_coords)
for x, y in boat3_coords:
    grid[y, x] = "2"

# print the grid with all boats
print(grid)