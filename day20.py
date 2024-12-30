from helpers import *

with open('day20_input.txt', 'r') as f:
    text = f.read().strip()

A = npa(lmap(list, text.split('\n')))
find = arr_find(A)
start = find('S')
end = find('E')
A[start] = '.'
A[end] = '.'
bounds = arr_bounds(A)

# pt1
def search(A):
    q = [(0, start)]
    pt = start
    seen = {start}
    while pt != end:
        dist, pt = heappop(q)
        for new_pos in grid_neighbors(pt):
            if new_pos not in seen and new_pos in bounds and A[new_pos] == '.':
                heappush(q, (dist+1, new_pos))
                seen.add(new_pos)
    return dist

base = search(A)
walls = npa(np.where(A == '#')).T
if input('Type "y" to compute part 1 result: ') == 'y':
    ct = 0
    for cheat in walls:
        A[*cheat] = '.'
        if base - search(A) >= 100:
            ct += 1
        A[*cheat] = '#'
    print(f'Part 1: {ct} cheats with at least 100 picoseconds saved')

# pt2
def path(A) -> List[Tuple[int, int]]:
    q = [(0, start, [start])]
    pt = start
    seen = {start}
    while q:
        dist, pt, path = heappop(q)
        if pt == end:
            return path
        for new_pos in grid_neighbors(pt):
            if new_pos not in seen and new_pos in bounds and A[new_pos] == '.':
                heappush(q, (dist+1, new_pos, path + [new_pos]))
                seen.add(new_pos)
    raise Exception('Did not find path')

def ksec_cheats(k, cheat_len=20) -> int:
    """ Returns # of cheats that save at least k secs """
    base_path = path(A)
    cheats = 0
    for i in range(len(base_path)-k-1):
        for j in range(i+k, len(base_path)):
            x1, y1 = base_path[i]
            x2, y2 = base_path[j]
            grid_dist = abs(x2 - x1) + abs(y2 - y1)
            if grid_dist <= cheat_len and j - i - grid_dist >= k:
                cheats += 1
    return cheats

print(f'Part 2: {ksec_cheats(100)} cheats with at least 100 picoseconds saved')