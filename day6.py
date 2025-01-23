from helpers import *

with open('day6_input.txt', 'r') as f:
    text = f.read().strip()

do_line = lambda line : [0 if c == '.' else (1 if c == '#' else 2) for c in line]
area = npa(lmap(do_line, text.split('\n')))
rows, cols = area.shape
start_pos = lmap(lambda a : a[0], np.where(area==2))
area[*start_pos] = 0
directions = ['up', 'right', 'down', 'left']
bounds = arr_bounds(area)

# pt1
def step(x : int, y : int, direction : int) -> Tuple[int, int]:
    new_x, new_y = x, y
    match directions[direction]:
        case 'up': new_x -= 1
        case 'right': new_y += 1
        case 'down': new_x += 1
        case _: new_y -= 1
    
    if (new_x, new_y) in bounds and area[new_x, new_y]:
        return (x, y, (direction + 1) % 4)
    return (new_x, new_y, direction)

visited = np.zeros(area.shape, dtype=int)
direction = 0
guard_x, guard_y = start_pos
while (guard_x, guard_y) in bounds:
    visited[guard_x, guard_y] = 1
    guard_x, guard_y, direction = step(guard_x, guard_y, direction)

print('Part 1:', visited.sum())

# pt2
def find_obstacles():
    res = 0
    ct = 0
    for x,y in bounds:
        ct += 1
        print(f'Progress: {ct} / {len(bounds)}', end='\r')
        if area[x, y] or (x, y) == start_pos:
            continue
        # try adding obstacle
        area[x, y] = 1
        direction = 0
        visited = set()
        guard_x, guard_y = start_pos
        while (guard_x, guard_y) in bounds:
            visited.add((guard_x, guard_y, direction))
            # find next loc
            guard_x, guard_y, direction = step(guard_x, guard_y, direction)
            # check for loop
            if (guard_x, guard_y, direction) in visited:
                res += 1
                break
        # undo obstacle
        area[x, y] = 0

    return res

print('\nPart 2:', find_obstacles())