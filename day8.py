from helpers import *

with open('day8_input.txt', 'r') as f:
    text = f.read().strip()

chars = set(text)
chars.remove('.')
A = npa(lmap(list, text.splitlines()))
bounds = arr_bounds(A)

# pt1
locs = set()
for char in chars:
    antennas = find(A, char)
    for a1, a2 in it.permutations(antennas, 2):
        diff = a1 - a2
        locs.add(tuple(a1 + diff))
        locs.add(tuple(a2 - diff))

print('Part 1:', sum(x in bounds for x in locs))

# pt2
lines = set()
for char in chars:
    antennas = find(A, char)
    for a1,a2 in it.permutations(antennas, 2):
        x1, y1 = a1
        x2, y2 = a2
        if x1 == x2:
            lines.add((x1, 0, 0, 0))
        else:
            slope = (y2 - y1) / (x2 - x1)
            lines.add((x1, y1, slope, 1))

locs2 = set()
for x, y in bounds:
    for x2, y2, m, flag in lines:
        if flag:
            if x != x2 and (y - y2) / (x - x2) == m:
                locs2.add((x,y))
                break
        elif x == x2:
            locs2.add((x,y))
            break

print('Part 2:', len(locs2))