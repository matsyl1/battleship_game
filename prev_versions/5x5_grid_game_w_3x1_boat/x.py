# 5x5 grid w single 3x1 boat

# import
import random
import numpy as np

# original grid
grid = np.full([5,5], ".", dtype=str)

# first coord of boat (coord1)
x1 = random.randint(0,4)
y1 = random.randint(0,4)
grid[y1, x1] = "1"

# 2nd and third coord (adjacent and same axis test).
def same_axis (coord1, coord2, coord3):
    x1, x2 = coord1
    x2, y2 = coord2
    x3, y3 = coord3
    return (x1==x2==x3) or (y1==y2==y3)
def adjacent_12 (coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return abs(x1-x2) + abs(y1-y2) == 1
def adjacent_13 (coord1, coord3):
    x1, y1 = coord1
    x3, y3 = coord3
    return abs(x1-x3) + abs(y1-y3) == 2
def adjacent_23 (coord2, coord3):
    x2, y2 = coord2
    x3, y3 = coord3
    return abs(x2-x3) + abs(y2-y3) == 1

while True:
    x2 = random.randint(0,4)
    y2 = random.randint(0,4)
    x3 = random.randint(0, 4)
    y3 = random.randint(0, 4)
    if adjacent_12((x1,y1),(x2,y2)) and adjacent_13((x1,y1),(x3,y3)) and adjacent_23((x2,y2),(x3,y3)) and ((x1==x2==x3) or (y1==y2==y3)):
        grid[y2, x2] = "2"
        grid[y3, x3] = "3"
        print(grid)
        break

