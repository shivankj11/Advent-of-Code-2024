from helpers import *

with open('day19_input.txt', 'r') as f:
    text = f.read().strip()

patterns, designs = text.split('\n\n')
patterns = set(patterns.split(', '))
designs = designs.splitlines()

# pt1
res1 = 0
for design in designs:
    f = {0}
    for j in range(1, len(design)+1):
        for i in range(j):
            if i in f and design[i:j] in patterns:
                f.add(j)
                break
    res1 += len(design) in f

print('Part 1:', res1)

# pt2
res2 = 0
for design in designs:
    f = {0 : 1}
    for j in range(1, len(design)+1):
        for i in range(j):
            if i in f and design[i:j] in patterns:
                f[j] = f.get(j, 0) + f[i]
    res2 += f.get(len(design), 0)

print('Part 2:', res2)