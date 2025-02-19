from helpers import *

with open('day15_input.txt', 'r') as f:
    text = f.read().strip()

maptext, movetext = text.split('\n\n')
dir_map = lambda s : {'>' : 0, 'v' : 1, '<' : 2, '^' : 3}[s]
moves = lmap(dir_map, movetext.replace('\n', ''))

# pt1
def simulate(A):
    x, y = find(A, '@', first=True)
    A[x, y] = '.'
    for direction in moves:
        step = grid_step(x, y, direction)
        if A[step] == '.':
            A[x, y] = '.'
            x, y = step
        elif A[step] == 'O':
            new_box = grid_step(*step, direction)
            while A[new_box] == 'O':
                new_box = grid_step(*new_box, direction)
            if A[new_box] == '.':
                A[new_box] = 'O'
                A[step] = '.'
                x, y = step
    return A

A = npa(lmap(list, maptext.splitlines()))
print('Part 1:', sum(100 * x + y for x,y in find(simulate(A), 'O')))

# pt2
def simulate_wide(A):
    x, y = find(A, '@', first=True)
    A[x, y] = '.'
    for direction in moves:
        step = grid_step(x, y, direction)
        if A[step] == '.':
            A[x, y] = '.'
            x, y = step
        elif A[step] == '[' or A[step] == ']':
            new_box = grid_step(*step, direction)
            while A[new_box] == '[' or A[new_box] == ']':
                new_box = grid_step(*new_box, direction)
            if A[new_box] == '.':
                if direction == 0: # right
                    for i in range(new_box[1], y, -1):
                        A[x, i] = A[x, i-1]
                    x, y = step
                elif direction == 2: # left
                    for i in range(new_box[1], y):
                        A[x, i] = A[x, i+1]
                    x, y = step
                elif direction == 1: # down
                    boxes = [step]
                    q = []
                    q.append(step)
                    if A[step] == '[':
                        q.append((step[0], step[1]+1))
                        boxes.append((step[0], step[1]+1))
                    else:
                        q.append((step[0], step[1]-1))
                        boxes.append((step[0], step[1]-1))
                    while q:
                        sx, sy = q.pop()
                        if A[sx+1, sy] == '[':
                            q.append((sx+1, sy))
                            boxes.append((sx+1, sy))
                            q.append((sx+1, sy+1))
                            boxes.append((sx+1, sy+1))
                        elif A[sx+1, sy] == ']':
                            q.append((sx+1, sy))
                            boxes.append((sx+1, sy))
                            q.append((sx+1, sy-1))
                            boxes.append((sx+1, sy-1))
                    blocked = False
                    for box in boxes:
                        bx, by = box
                        if A[bx+1, by] == '#':
                            blocked = True
                    if not blocked:
                        seen = set()
                        for box in boxes[::-1]:
                            if box not in seen:
                                bx, by = box
                                A[bx+1, by] = A[box]
                                A[box] = '.'
                                seen.add(box)
                        x, y = step
                else : # up
                    boxes = [step]
                    q = []
                    q.append(step)
                    if A[step] == '[':
                        q.append((step[0], step[1]+1))
                        boxes.append((step[0], step[1]+1))
                    else:
                        q.append((step[0], step[1]-1))
                        boxes.append((step[0], step[1]-1))
                    while q:
                        sx, sy = q.pop()
                        if A[sx-1, sy] == '[':
                            q.append((sx-1, sy))
                            boxes.append((sx-1, sy))
                            q.append((sx-1, sy+1))
                            boxes.append((sx-1, sy+1))
                        elif A[sx-1, sy] == ']':
                            q.append((sx-1, sy))
                            boxes.append((sx-1, sy))
                            q.append((sx-1, sy-1))
                            boxes.append((sx-1, sy-1))
                    blocked = False
                    for box in boxes:
                        bx, by = box
                        if A[bx-1, by] == '#':
                            blocked = True
                    if not blocked:
                        seen = set()
                        for box in boxes[::-1]:
                            if box not in seen:
                                bx, by = box
                                A[bx-1, by] = A[box]
                                A[box] = '.'
                                seen.add(box)
                        x, y = step
    return A

wide_map = lambda c : {'O' : '[]', '#' : '##', '.' : '..', '@' : '@.'}[c]
A_wide = lmap_nested(wide_map, maptext.splitlines())
A_wide = npa(lmap(lambda v : list(''.join(v)), A_wide))
print('Part 2:', sum(100 * x + y for x,y in find(simulate_wide(A_wide), '[')))