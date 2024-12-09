from helpers import *

with open('day9_input.txt', 'r') as f:
    text = f.read().strip()

L = lmap(int, text)
L = lmap(lambda i : L[i] if i % 2 else (L[i], i // 2), range(len(L)))

# pt1
def get_arr():
    space = []
    for i in range(len(L)):
        if i % 2:
            for _ in range(L[i]):
                space.append(-1)
        else:
            n, idx = L[i]
            for _ in range(n):
                space.append(idx)
    i = 0
    while i < len(space):
        if space[i] == -1:
            while space[-1] == -1:
                if i >= len(space) - 1:
                    space.pop()
                    return space
                space.pop()
            n = space[-1]
            space[i] = n
            space.pop()
        i += 1
    return space

r = get_arr()
print(sum(x * y for x,y in zip(r, range(len(r)))))

# pt2
j = len(L) - 1
while j >= 0:
    if type(L[j]) is int:
        j -= 1
        continue
    n, idx = L[j]
    for i in range(1, j):
        if type(L[i]) is int and L[i] >= n:
            L[j] = (n, 0)
            if n < L[i]:
                L.insert(i+1, L[i] - n)
            L[i] = (n, idx)
            break
    j -= 1

r2 = []
for v in L:
    if type(v) is int:
        for _ in range(v):
            r2.append(0)
    else:
        n, idx = v
        for _ in range(n):
            r2.append(idx)

print(sum(x * y for x,y in zip(r2, range(len(r2)))))
