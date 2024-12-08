from helpers import *

with open('day5_input.txt', 'r') as f:
    text = f.read()

rules, updates = text.split('\n\n')
rules = [lmap(int, line.split('|')) for line in rules.split('\n')]
updates = [lmap(int, line.split(',')) for line in updates.split('\n')]

def wrong(line : List[int]) -> bool:
    for before, after in rules:
        if (before in line and after in line and
            line.index(before) > line.index(after)):
                return True
    return False

# pt1
res1 = sum(map(median, it.filterfalse(wrong, updates)))
print(res1)

# pt2
wrong_lines = list(filter(wrong, updates))
for line in wrong_lines:
    while wrong(line):
        for before, after in rules:
            if before in line and after in line:
                xidx, yidx = line.index(before), line.index(after)
                if xidx > yidx:
                    line[xidx] += line[yidx]
                    line[yidx] = line[xidx] - line[yidx]
                    line[xidx] -= line[yidx]

res2 = sum(map(median, wrong_lines))
print(res2)