# create 5x5 grid game, one randomly placed 1x2 target, loop user hits until sink

# import
import numpy as np
import random

# original 5x5 grid
grid = np.full((5, 5), ".", dtype=str)

# first random cord.
rand_x = random.randint(0,4)
rand_y = random.randint(0,4)
# grid[rand_y,rand_x] = 1

# adjacent check
def adjacent (coord1,coord2):
    x, y = coord1
    x2, y2 = coord2
    return abs(x-x2) + abs(y-y2) == 1

# loop to place second coord only when adjacent to first coord
while True:
    rand2_x = random.randint(0,4)
    rand2_y = random.randint(0,4)
    if adjacent((rand_x,rand_y),(rand2_x, rand2_y)):
        # grid[rand2_y, rand2_x] = 1
        # print(grid)
        break

# set to keep track of remaining, non-hit coord.
remaining_coord = {(rand_x, rand_y), (rand2_x, rand2_y)}

# user input loop
print("Game on, fire away!")
while remaining_coord:
    x = int(input("Type x-cord: "))
    y = int(input("Type y-cord: "))

    if (x, y) in remaining_coord:
        print("Hit!")
        grid[y, x] = "H"
        print(grid)
        remaining_coord.remove((x, y))
    else:
        print("Miss, try again.")
        grid[y, x] = "m"
        print(grid)

# check if remaining_coord set is empty and if true, game over
if not remaining_coord:
    print("You sunk the boat! Game over.")



