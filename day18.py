from helpers import *

with open('day18_input.txt', 'r') as f:
    text = f.read()

falling = lmap(partial(lmap, int), (v.split(',') for v in text.strip().split('\n')))
falling = npa(falling)

# pt1
A = np.zeros((71, 71))
bounds = arr_bounds(A)
for x,y in falling[:1024]:
    A[x,y] = 1

def search():
    q = [(0, 0)]
    ct = 0
    seen = set()
    while True:
        new = []
        for x,y in q:
            filterfn = lambda v : v not in seen and v in bounds and not A[v]
            for n in filter(filterfn, grid_neighbors((x,y))):
                if n == (70, 70):
                    return ct + 1
                new.append(n)
                seen.add(n)
        q = new
        ct += 1

print(search())

# pt2
def search2(A) -> bool:
    q = [(0, 0)]
    ct = 0
    seen = set()
    while q:
        new = []
        for x,y in q:
            filterfn = lambda v : v not in seen and v in bounds and not A[v]
            for n in filter(filterfn, grid_neighbors((x,y))):
                if n == (70, 70):
                    return True
                new.append(n)
                seen.add(n)
        q = new
        ct += 1
    return False

for byte in falling[1024:]:
    A[*byte] = 1
    if not search2(A):
        print(byte)
        break