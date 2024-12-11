from helpers import *

with open('day8_input.txt', 'r') as f:
    text = f.read().strip()

chars = set(text)
chars.remove('.')
A = npa(lmap(list, text.split('\n')))
rows, cols = A.shape
idxs = list(mesh(rows, cols))

# pt1
locs = set()
for char in chars:
    antennas = npa(np.where(A == char)).T
    for a1,a2 in it.product(antennas, antennas):
        if (a1 == a2).all():
            continue
        diff = a1 - a2
        locs.add(tuple(a1 + diff))
        locs.add(tuple(a2 - diff))

locs_ct = sum(lmap(lambda x : 1 if x in idxs else 0, locs))
print(locs_ct)

# pt2
lines = set()
for char in chars:
    antennas = npa(np.where(A == char)).T
    for a1,a2 in it.product(antennas, antennas):
        if (a1 == a2).all():
            continue
        x1, y1 = a1
        x2, y2 = a2
        if x1 == x2:
            lines.add((None, x1, 1))
        else:
            slope = (y2 - y1) / (x2 - x1)
            lines.add((slope, (x1, y1), 0))

locs2 = set()
for x, y in idxs:
    for line in lines:
        x2, y2 = line[1]
        if line[-1]:
            if x == x2:
                locs2.add((x,y))
                break
        else:
            if x == x2:
                continue
            if x == x2 and y == y2:
                locs2.add((x,y))
                break
            if (y - y2) / (x - x2) == line[0]:
                locs2.add((x,y))
                break

print(len(locs2))