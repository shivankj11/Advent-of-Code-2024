from helpers import *

with open('day17_input.txt', 'r') as f:
    text = f.read().strip()

text = '''###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############'''
A = npa(lmap(partial(lmap, identity), text.split('\n')))
bounds = bounds(A)
start = npa(np.where(A == 'S')).T[0]

# pt1
def search(start):
    q = [(0, start)] # min heap
    seen = set()
    filterfn = lambda v : v not in seen and v[1] in bounds and A[v[1]] != '#'
    while q:
        prio, pos = heappop(q)
        pt, direction = pos
        if A[pt] == 'E':
            return prio
        for n in filter(filterfn, grid_neighbors(pt)):
            seen.add((n, direction))
            heappush(q, (prio+1, (n, direction)))
        

return search(start)