# create a 2x2 grid, let computer randomly pick a location and let the user keep guessing until hit

# import
import numpy
import random

# random target
Rand_x = random.randrange(0, 2, 1)
Rand_y = random.randrange(0, 2, 1)

# original grid
grid = numpy.zeros([2,2])
print(grid)

# loop counter/attempts + possible attempts
loop_count = 0
max_attempts = len(grid)*len(grid)

# round x loop
Hx = "x-cord pick"
Hy = "y-cord pick"
while Hx != Rand_x or Hy != Rand_y:
    Hx = int(input("Type x-cord. (0-1): "))
    Hy = int(input("Type y-cord. (0-1): "))
    grid[Hx, Hy] = 1
    loop_count = loop_count + 1
    print(grid)
    if Hx == Rand_x and Hy == Rand_y:
      print("Bingo! (Took you", loop_count, "out of", max_attempts, "attempts)")

