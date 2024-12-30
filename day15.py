from helpers import *

with open('day15_input.txt', 'r') as f:
    text = f.read().strip()

maptext, movetext = text.split('\n\n')
A = npa(lmap(list, maptext.splitlines()))
dir_map = {'>' : 0, 'v' : 1, '<' : 2, '^' : 3}
moves = lmap(lambda s : dir_map[s], movetext.replace('\n', ''))

# pt1
x, y = npa(np.where(A == '@')).T[0]
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

res1 = sum(100 * x + y for x, y in npa(np.where(A == 'O')).T)
print(res1)

# pt2
wide_map = {'O' : '[]', '#' : '##', '.' : '..', '@' : '@.'}
A2 = lmap(partial(map, lambda c : wide_map[c]), maptext.splitlines())
A2 = npa(lmap(list, npa(["".join(v) for v in A2])))
x, y = npa(np.where(A2 == '@')).T[0]
print(A2)
A2[x, y] = '.'
for direction in moves:
    step = grid_step(x, y, direction)
    if A2[step] == '.':
        A2[x, y] = '.'
        x, y = step
    elif A2[step] == '[' or A2[step] == ']':
        new_box = grid_step(*step, direction)
        while A2[new_box] == '[' or A2[new_box] == ']':
            new_box = grid_step(*new_box, direction)
        if A2[new_box] == '.':
            if direction == 0: # right
                for i in range(new_box[1], y, -1):
                    A2[x, i] = A2[x, i-1]
                x, y = step
            elif direction == 2: # left
                for i in range(new_box[1], y):
                    A2[x, i] = A2[x, i+1]
                x, y = step
            elif direction == 1: # down
                boxes = [step]
                q = []
                q.append(step)
                if A2[step] == '[':
                    q.append((step[0], step[1]+1))
                    boxes.append((step[0], step[1]+1))
                else:
                    q.append((step[0], step[1]-1))
                    boxes.append((step[0], step[1]-1))
                while q:
                    sx, sy = q.pop()
                    if A2[sx+1, sy] == '[':
                        q.append((sx+1, sy))
                        boxes.append((sx+1, sy))
                        q.append((sx+1, sy+1))
                        boxes.append((sx+1, sy+1))
                    elif A2[sx+1, sy] == ']':
                        q.append((sx+1, sy))
                        boxes.append((sx+1, sy))
                        q.append((sx+1, sy-1))
                        boxes.append((sx+1, sy-1))
                blocked = False
                for box in boxes:
                    bx, by = box
                    if A2[bx+1, by] == '#':
                        blocked = True
                if not blocked:
                    seen = set()
                    for box in boxes[::-1]:
                        if box not in seen:
                            bx, by = box
                            A2[bx+1, by] = A2[box]
                            A2[box] = '.'
                            seen.add(box)
                    x, y = step
            else : # up
                boxes = [step]
                q = []
                q.append(step)
                if A2[step] == '[':
                    q.append((step[0], step[1]+1))
                    boxes.append((step[0], step[1]+1))
                else:
                    q.append((step[0], step[1]-1))
                    boxes.append((step[0], step[1]-1))
                while q:
                    sx, sy = q.pop()
                    if A2[sx-1, sy] == '[':
                        q.append((sx-1, sy))
                        boxes.append((sx-1, sy))
                        q.append((sx-1, sy+1))
                        boxes.append((sx-1, sy+1))
                    elif A2[sx-1, sy] == ']':
                        q.append((sx-1, sy))
                        boxes.append((sx-1, sy))
                        q.append((sx-1, sy-1))
                        boxes.append((sx-1, sy-1))
                blocked = False
                for box in boxes:
                    bx, by = box
                    if A2[bx-1, by] == '#':
                        blocked = True
                if not blocked:
                    seen = set()
                    for box in boxes[::-1]:
                        if box not in seen:
                            bx, by = box
                            A2[bx-1, by] = A2[box]
                            A2[box] = '.'
                            seen.add(box)
                    x, y = step

res2 = sum(100 * x + y for x, y in npa(np.where(A2 == '[')).T)
print(res2)