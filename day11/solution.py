from itertools import count
import numpy as np


def neighbour_indices(r, c):
    return np.s_[max(0, r-1):r+2, max(0, c-1):c+2]


def simulate_one_step(grid):
    grid += 1
    
    flashes = np.zeros(dtype='bool', shape=grid.shape)
    while True:
        new_flashes = False
        for r in range(grid.shape[0]):
            for c in range(grid.shape[1]):
                if grid[r, c] > 9 and not flashes[r, c]:
                    flashes[r, c] = True
                    new_flashes = True
                    grid[neighbour_indices(r, c)] += 1
        if not new_flashes:
            break

    grid[flashes] = 0
    return sum(flashes.flat)


def day11a(grid, days):
    return sum(simulate_one_step(grid) for _ in range(days))


def day11b(grid):
    for day in count(1):
        if simulate_one_step(grid) == grid.size:
            return day


if __name__ == '__main__':
    grid = np.asarray([list(map(int, line.strip())) for line in open('day11/input.txt')])
    print(day11a(grid.copy(), 100))
    print(day11b(grid))
