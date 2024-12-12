from helpers import *

with open('day10_input.txt', 'r') as f:
    text = f.read().strip()

A = npa([lmap(int, list(line)) for line in text.split('\n')])
rows, cols = A.shape
bounds = list(mesh(rows, cols))

def bfs(neighbor_fn, pt) -> int:
    q = [pt]
    curr = 0
    while curr < 9:
        curr += 1
        neighbors = neighbor_fn(q)
        q = list(filter(lambda pt : pt in bounds and A[pt] == curr, neighbors))
    return len(q)

collect = lambda nfn : sum(map(partial(bfs, nfn), filter(lambda x : not A[*x], mesh(rows, cols))))
# pt1: sum of # 9 reachable for all 0s
res1 = collect(lambda q : reduce(lambda x, y : x.union(y), lmap(grid_neighbors, q), set()))
print(f'Pt1 Result: {res1}\n')

# pt2: sum of # distinct paths 0->9 for all 0s
res2 = collect(lambda q : reduce(op.add, lmap(grid_neighbors, q), []))
print(f'Pt2 Result: {res2}\n')