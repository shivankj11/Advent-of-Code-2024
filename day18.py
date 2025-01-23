from helpers import *

with open('day18_input.txt', 'r') as f:
    text = f.read().strip()

falling = npa(lmap_nested(int, (v.split(',') for v in text.splitlines())))

# pt1
A = np.zeros((71, 71))
A[*falling[:1024].T] = 1
bounds = arr_bounds(A)

def search(A) -> int:
    """
        RETURNS
            Length of shortest path from (0,0) -> (70,70) if it
            exists and False otherwise
    """
    q = [(0, 0)]
    ct = 1
    seen = set()
    while q:
        new = []
        for x,y in q:
            filterfn = lambda v : v not in seen and v in bounds and not A[v]
            for n in filter(filterfn, grid_neighbors((x,y))):
                if n == (70, 70):
                    return ct
                new.append(n)
                seen.add(n)
        q = new
        ct += 1
    return False

print('Part 1:', search(A))

# pt2
for byte in falling[1024:]:
    A[*byte] = 1
    if not search(A):
        break

print('Part 2:', byte)