from helpers import *

with open('day6_input.txt', 'r') as f:
    text = f.read().strip()

do_line = lambda line : [0 if c == '.' else (1 if c == '#' else 2) for c in line]
area = npa(lmap(do_line, text.split('\n')))
rows, cols = area.shape
start_pos = lmap(lambda a : a[0], np.where(area==2))
area[*start_pos] = 0
directions = ['up', 'right', 'down', 'left']
idx = set(mesh(rows, cols))

# pt1
def step(x : int, y : int, direction : int) -> Tuple[int, int]:
    new_x, new_y = x, y
    if directions[direction] == 'up':
        new_x -= 1
    elif directions[direction] == 'right':
        new_y += 1
    elif directions[direction] == 'down':
        new_x += 1
    else:
        new_y -= 1
    
    if (new_x, new_y) in idx and area[new_x, new_y]:
        return (x, y, (direction + 1) % 4)
    return (new_x, new_y, direction)

visited = np.zeros(area.shape, dtype=int)
direction = 0
guard_x, guard_y = start_pos
while (guard_x, guard_y) in idx:
    visited[guard_x, guard_y] = 1
    guard_x, guard_y, direction = step(guard_x, guard_y, direction)

print(visited.sum())

# pt2
res2 = 0
ct = 0
for x,y in idx:
    ct += 1
    print(f'Progress: {ct} / {len(idx)}', end='\r')
    if area[x, y] or (x, y) == start_pos:
        continue
    # try adding obstacle
    area[x, y] = 1
    direction = 0
    visited = set()
    guard_x, guard_y = start_pos
    while (guard_x, guard_y) in idx:
        visited.add((guard_x, guard_y, direction))
        # find next loc
        guard_x, guard_y, direction = step(guard_x, guard_y, direction)
        # check for loop
        if (guard_x, guard_y, direction) in visited:
            res2 += 1
            break

    # undo obstacle
    area[x, y] = 0

print('\n')
print(res2)