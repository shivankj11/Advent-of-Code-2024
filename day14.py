from helpers import *

with open('day14_input.txt', 'r') as f:
    text = f.read()

robots = text.strip().splitlines()
for i in range(len(robots)):
    pos, vel = robots[i].split(' ')
    pos = lmap(int, pos[2:].split(','))
    vel = lmap(int, vel[2:].split(','))
    robots[i] = (pos, vel)

# pt1
A = np.zeros((103, 101))
for pos, vel in robots:
    x = (pos[0] + 100 * vel[0]) % A.shape[1]
    y = (pos[1] + 100 * vel[1]) % A.shape[0]
    A[y,x] += 1

res1 = A[:51,:50].sum() * A[:51,51:].sum() * A[52:,:50].sum() * A[52:,51:].sum()
print(res1)

# pt2
ct = 6500
while True:
    A = np.full((103, 101), ' ')
    for pos, vel in robots:
        x = (pos[0] + ct * vel[0]) % A.shape[1]
        y = (pos[1] + ct * vel[1]) % A.shape[0]
        A[y,x] = 'X'
    print(ct)
    for line in A:
        print(line.tolist())
    ct += 1
    time.sleep(.15)

# 6771