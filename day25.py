from helpers import *

with open('day25_input.txt', 'r') as f:
    text = f.read().strip()

grids = lmap_nested(list, map(str.splitlines, text.split('\n\n')))
lock_grids = [npa(grid).T for grid in grids if grid[0][0] == '#']
locks = lmap_nested(lambda v : arr_find(v)('.'), lock_grids)
key_grids = [npa(grid).T for grid in grids if grid[0][0] == '.']
keys = lmap_nested(lambda v : arr_find(v)('#'), key_grids)

# pt1
ct = 0
for key,lock in it.product(keys, locks):
    ct += all(k >= l for k,l in zip(key, lock))

print('Answer:', ct)