from helpers import *

with open('day10_input.txt', 'r') as f:
    text = f.read().strip()

A = npa([lmap(int, list(line)) for line in text.split('\n')])
rows, cols = A.shape
bounds = list(mesh(rows, cols))

# pt1: sum of # 9 reachable for all 0s
def get_neighbors(pt):
    x, y = pt
    return {(x+1, y), (x-1,y), (x,y+1), (x,y-1)}

def bfs(x : int, y : int) -> int:
    """ Returns True iff 9 reachable from (x,y) """
    q = [(x, y)]
    curr = 0
    tot = 0
    while q:
        neighbors = reduce(lambda x, y : x.union(y), lmap(get_neighbors, q))
        q = []
        for x,y in neighbors:
            if (x,y) in bounds and A[x,y] == curr + 1:
                if curr + 1 == 9:
                    tot += 1
                else:
                    q.append((x,y))
        curr += 1
    return tot

res1 = 0
ct = 0
for i,j in mesh(rows, cols):
    ct += 1
    print(f'Progress: {ct} / {rows * cols}', end='\r')
    if A[i, j] == 0:
        res1 += bfs(i, j)

print('\n')
print(res1)

# pt2: sum of # distinct paths 0->9 for all 0s
def dfs(x : int, y : int) -> int:
    paths = 0
    q = [(x, y, 0)]
    while q:
        x, y, curr = q.pop()
        for x2, y2 in filter(lambda v : v in bounds, get_neighbors((x,y))):
            if A[x2, y2] == curr + 1:
                if curr + 1 == 9:
                    paths += 1
                else:
                    q.append((x2, y2, curr+1))
    return paths

res2 = 0
ct = 0
for i,j in mesh(rows, cols):
    ct += 1
    print(f'Progress: {ct} / {rows * cols}', end='\r')
    if A[i, j] == 0:
        res2 += dfs(i, j)

print('\n')
print(res2)