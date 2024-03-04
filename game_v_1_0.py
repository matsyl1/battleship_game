# imports
import random
import numpy as np

# grid for boat placement
grid = np.full([8, 8], ".", dtype=str)

# empty list to keep track of all boat coords
used_coords = []

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
        x1, y1 = random.randint(0, 8 - size), random.randint(0, 8 - size)
        # boat direction (horizontal/vertical)
        if random.choice([True, False]):
            (x2, y2) = x1 + size - 1, y1
        else:
            (x2, y2) = x1, y1 + size - 1

        # boat coords (middle)
        new_coords = [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]
        if not overlap(used_coords, new_coords):
            return [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]

# generate boats
def generate_boats():
    # empty list to track used coords
    global used_coords
    used_coords = []
    # loop thru boats
    for size in range(1, 6):
        boat = create_boat_coords(size, used_coords)
        for (x, y) in boat:
            grid[y, x] = size
        # extend list of used coords
        used_coords.extend(boat)
    # print(grid)
    # print(used_coords)
generate_boats()

# NEW: game logic-----------------------------------------------------------------------------------
# store each boat coords in separate list
boat1 = used_coords[:1]
boat2 = used_coords[1:3]
boat3 = used_coords[3:6]
boat4 = used_coords[6:10]
boat5 = used_coords[10:15]

# store hits and misses in empty list and append with new strikes
hits = []
misses = []

# game grid to display hits/misses
grid_hit_miss = np.full([8, 8], ".", dtype=str)

# strike logic (hit, miss, boat sunk message)
for _ in range(64):
    strike = input("Select coord (y, x) you'd like to strike: ")
    strike = tuple(map(int, strike.split(',')))
    if strike in used_coords:
        print("Hit")
        hits.append(strike)
        grid_hit_miss[strike] = "X"
        print(grid_hit_miss)
        if all(i in hits for i in boat1):
            print("You've sunk boat 1")
        if all(i in hits for i in boat2):
            print("You've sunk boat 2")
        if all(i in hits for i in boat3):
            print("You've sunk boat 3")
        if all(i in hits for i in boat4):
            print("You've sunk boat 4")
        if all(i in hits for i in boat5):
            print("You've sunk boat 5")
        if all(i in hits for i in used_coords):
            print("Game over - you've sunk all boats!")
            exit()
    else:
        print("Miss")
        misses.append(strike)
        grid_hit_miss[strike] = "o"
        print(grid_hit_miss)

    # print(f"used_coords:", used_coords)
    print(f"hits:", hits)
    print(f"misses:", misses)