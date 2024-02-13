# 5x5 grid w single 4x1 boat

# import
import random
import numpy as np

# original grid
grid = np.full([5,5], ".", dtype=str)

# first coord of boat (coord1)
x1 = random.randint(0,4)
y1 = random.randint(0,4)
grid[y1, x1] = "4"

# all random coords must be on same axis
def same_axis (coord1, coord2, coord3, coord4):
    x1, x2 = coord1
    x2, y2 = coord2
    x3, y3 = coord3
    x4, y4 = coord4
    return (x1==x2==x3==x4) or (y1==y2==y3==y4)

# adjacent condition for coord1 and coord2
def adjacent_12 (coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return abs(x1-x2) + abs(y1-y2) == 1

# adjacent condition for coord1 and coord3
def adjacent_13 (coord1, coord3):
    x1, y1 = coord1
    x3, y3 = coord3
    return abs(x1-x3) + abs(y1-y3) == 2

# adjacent condition for coord2 and coord3
def adjacent_23 (coord2, coord3):
    x2, y2 = coord2
    x3, y3 = coord3
    return abs(x2-x3) + abs(y2-y3) == 1

# adjacent condition for coord1 and coord4
def adjacent_14 (coord1, coord4):
    x1, y1 = coord1
    x4, y4 = coord4
    return abs(x1-x4) + abs(y1-y4) == 3

while True:
    x2 = random.randint(0,4)
    y2 = random.randint(0,4)
    x3 = random.randint(0, 4)
    y3 = random.randint(0, 4)
    x4 = random.randint(0, 4)
    y4 = random.randint(0, 4)
    if adjacent_12((x1,y1),(x2,y2)) and adjacent_13((x1,y1),(x3,y3)) and adjacent_23((x2,y2),(x3,y3)) and adjacent_14((x1,y1),(x4,y4)) and ((x1==x2==x3==x4) or (y1==y2==y3==y4)):
        grid[y2, x2] = "4"
        grid[y3, x3] = "4"
        grid[y4, x4] = "4"
        print(grid)
        break
