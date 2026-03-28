import random
import time
import os

WIDTH = 20
HEIGHT = 20

def create_grid():
    grid = []
    for i in range(HEIGHT):
        row = []
        for j in range(WIDTH):
            row.append(random.randint(0, 1))
        grid.append(row)
    return grid

def count_LiveNeighbours(grid, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= x + i < HEIGHT and 0 <= y + j < WIDTH:
                count += grid[x + i][y + j]
    return count

def check(grid):
    new_grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for i in range(HEIGHT):
        for j in range(WIDTH):
            neighbors = count_LiveNeighbours(grid, i, j)

            if grid[i][j] == 0 and neighbors == 3:
                new_grid[i][j] = 1
            elif grid[i][j] == 1 and neighbors in (2, 3):
                new_grid[i][j] = 1
            else:
                new_grid[i][j] = 0

    return new_grid

def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
            print(" ".join(str(cell) for cell in row))

def main():
    grid = create_grid()

    while True:
        print_grid(grid)
        grid = check(grid)
        time.sleep(1)

if __name__ == "__main__":
    main()