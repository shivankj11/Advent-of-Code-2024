from helpers import *

with open('day25_input.txt', 'r') as f:
    text = f.read().strip()

grids = [lmap(list, grid.splitlines()) for grid in text.split('\n\n')]
lock_grids = [npa(grid) for grid in grids if grid[0][0] == '#']
rows, cols = lock_grids[0].shape
locks = [[arr_find(row)('.')[0] for row in lock.T] for lock in lock_grids]
key_grids = [npa(grid) for grid in grids if grid[0][0] == '.']
keys = [[arr_find(row)('#')[0] for row in key.T] for key in key_grids]

# pt1
ct = 0
for key, lock in it.product(keys, locks):
    ct += all(k >= l for k,l in zip(key, lock))

print('Answer:', ct)