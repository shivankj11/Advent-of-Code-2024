from helpers import *

with open('day9_input.txt', 'r') as f:
    text = f.read().strip()

L = list(enumerate(lmap(int, text)))

# pt1
def get_mem():
    space = []
    for i,n in L:
        val = -1 if i % 2 else i // 2
        for _ in range(n):
            space.append(val)
    i = 0
    while i < len(space):
        if space[i] == -1:
            while space[-1] == -1 and i < len(space)-1:
                space.pop()
            space[i] = space[-1]
            space.pop()
        i += 1
    return space

print('Part 1:', sum(x * y for x,y in enumerate(get_mem())))

# pt2
def get_mem2():
    j = len(L)
    while j > 0:
        j -= 1
        idx, n = L[j]
        if idx % 2:
            continue
        for i in range(1, j):
            idx2, n2 = L[i]
            if idx2 % 2 and n2 >= n:
                # push L[j] mem into L[i] if space
                L[j] = (0, n)
                L[i] = (idx, n)
                if n < n2:
                    L.insert(i+1, (-1, n2 - n))
                break
    spaces = []
    for idx, n in L:
        val = 0 if idx % 2 else idx // 2
        for _ in range(n):
            spaces.append(val)
    return spaces

print('Part 2:', sum(x * y for x,y in enumerate(get_mem2())))
