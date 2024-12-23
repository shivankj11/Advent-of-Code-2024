from helpers import *

with open('day16_input.txt', 'r') as f:
    text = f.read().strip()

A = npa(lmap(partial(lmap, identity), text.split('\n')))
bounds = arr_bounds(A)
start = tuple(npa(np.where(A == 'S')).T[0])

# pt1
def search(start) -> int:
    """
    Direction 0 = E, 1 = S, 2 = W, 3 = N
    Returns score of best path
    """
    q = [(0, (start, 0))] # min heap
    seen = {(start, 0)}
    while q:
        prio, pos = heappop(q)
        pt, direction = pos
        x, y = pt
        if A[pt] == 'E':
            return prio
        # add move forward
        step = grid_step(x, y, direction)
        if (step, direction) not in seen and step in bounds and A[step] != '#':
            seen.add((step, direction))
            heappush(q, (prio+1, (step, direction)))
        # add pivot clockwise
        if (pt, (direction + 1) % 4) not in seen:
            seen.add((pt, (direction + 1) % 4))
            heappush(q, (prio+1000, (pt, (direction + 1) % 4)))
        # add pivot counter-clockwise
        if (pt, (direction - 1) % 4) not in seen:
            seen.add((pt, (direction - 1) % 4))
            heappush(q, (prio+1000, (pt, (direction - 1) % 4)))

    raise Exception("No path found from S->E")

print(search(start))

# pt2
def search2(start) -> int:
    """
    Direction 0 = E, 1 = S, 2 = W, 3 = N
    Returns number of tiles on all best paths
    """
    best_score = search(start)
    q = [(0, (start, 0), {(start, 0)})] # min heap
    tiles_on_best = set()
    seen = {}
    while q:
        prio, pos, path = heappop(q)
        if prio > best_score or pos in seen and seen[pos] < prio:
            continue
        pt, direction = pos
        x, y = pt
        if A[pt] == 'E':
            for tile,_ in path:
                tiles_on_best.add(tile)
            continue
        # add move forward
        step = grid_step(x, y, direction)
        new_pos = (step, direction)
        if (new_pos not in seen or seen[new_pos] >= prio + 1) and step in bounds and A[step] != '#':
            seen[new_pos] = prio+1
            new_path = deepcopy(path)
            new_path.add(new_pos)
            heappush(q, (prio+1, new_pos, new_path))
        # add pivot clockwise
        new_pos = (pt, (direction + 1) % 4)
        if new_pos not in seen or seen[new_pos] >= prio + 1000:
            seen[new_pos] = prio+1000
            new_path = deepcopy(path)
            new_path.add(new_pos)
            heappush(q, (prio+1000, new_pos, new_path))
        # add pivot counter-clockwise
        new_pos = (pt, (direction - 1) % 4)
        if new_pos not in seen or seen[new_pos] >= prio + 1000:
            seen[new_pos] = prio+1000
            new_path = deepcopy(path)
            new_path.add(new_pos)
            heappush(q, (prio+1000, new_pos, new_path))

    return len(tiles_on_best)

print(search2(start))